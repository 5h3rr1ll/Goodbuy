import json

import requests
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rq import Queue

from goodbuyDatabase.models import (
    BigTen,
    Brand,
    Company,
    Corporation,
    Country,
    MainProductCategory,
    Product,
    ProductCategory,
    SubProductCategory,
)
from scraper.aws_lambda_cc_crawler import scrape
from scraper.django_cc_crawler import Scraper as local_scraper
from worker import conn

q = Queue(connection=conn)


def is_product_in_db(request, code):
    return HttpResponse(str(Product.objects.filter(code=code).exists()))


def is_big_ten_by_name(request, brand_name):
    if brand_name == "":
        return "We don't know"
    try:
        brand = Brand.objects.get(name=brand_name)
        if brand.corporation:
            return BigTen.objects.filter(name=brand.corporation).exists()
        else:
            return "We don't know"
    except Exception as e:
        print(str(e))
        brand = Brand.objects.filter(name__trigram_similar=brand_name)[0]
        if brand.corporation:
            return BigTen.objects.filter(
                name__trigram_similar=brand.corporation
            ).exists()
        else:
            return "We don't know"


def is_big_ten_by_code(request, code):
    product = Product.objects.get(code=code)
    if product.brand is None:
        return "We don't know"
    print(f"Product Brand: {product.brand}")
    if product.data_source == "1":
        print(product.brand)
        answer = off_brand_checker(request, product.brand)
        return answer
    brand = Brand.objects.filter(name__trigram_similar=product.brand)[0]
    print(f"Trigram Similar Brand: {product.brand}")
    print(f"New Brand: {brand}")
    if brand.corporation:
        print(f"Brand Corp: {brand.corporation}")
        return HttpResponse(BigTen.objects.filter(name__trigram_similar=brand.corporation).exists())
    return HttpResponse(False)


def check_for_attributes(request, product_object):
    try:
        brand = product_object.brand.name
    except Exception as e:
        brand = ""
        print("Error in check for attributes: ", str(e))
    try:
        corporation = product_object.brand.corporation.name
    except Exception as e:
        corporation = ""
        print("Error in check for attributes: ", str(e))
    try:
        sub_product_category = product_object.sub_product_category.name
    except Exception as e:
        sub_product_category = ""
        print("Error in check for attributes: ", str(e))
    return (brand, corporation, sub_product_category)


# Creates feedback string but also returns it with the product_object
def create_feedback_string(request, product_object):
    open_food_facts = "1"
    brand, corporation, sub_product_category = check_for_attributes(
        request, product_object
    )
    product_serialized = serializers.serialize("json", [product_object])
    product_serialized = product_serialized.strip("[]")
    product_serialized = json.loads(product_serialized)
    product_serialized["fields"]["brand"] = brand
    product_serialized["fields"]["corporation"] = corporation
    product_serialized["fields"]["sub_product_category"] = sub_product_category
    if product_object.data_source == open_food_facts:
        lst_names = brand.split(",")
        first = is_big_ten_by_name(request, lst_names[0].strip())
        if first:
            product_serialized["is_big_ten"] = first
            return product_serialized
        else:
            try:
                second = is_big_ten_by_name(request, lst_names[1].strip())
                if second:
                    product_serialized["is_big_ten"] = second
                    return product_serialized
            except Exception as e:
                print(str(e))
                product_serialized["is_big_ten"] = False
                return product_serialized
    else:
        product_serialized["is_big_ten"] = is_big_ten_by_name(request, brand)
        return product_serialized


def feedback(request, code):
    # looks if product exist in database
    if request.method == "GET" and Product.objects.filter(code=code).exists():
        product_object = Product.objects.get(code=code)
        product_object.scanned_counter += 1
        product_object.save()
        if product_object.state == "209":
            print("Code is already in progress")
            return HttpResponse(status=209)
        # product exists calls for string creation and then returns json answer
        answer = create_feedback_string(request, product_object)
        return JsonResponse(answer)
    print(f"Looking up OFF for code {code}")
    response = requests.get(
        f"https://world.openfoodfacts.org/api/v0/product/{code}.json"
    )
    response_as_json = json.loads(response.text)
    if response_as_json["status_verbose"] == "product found":
        print("\nGot product from OFF\n")
        try:
            brand, created = Brand.objects.get_or_create(
                name=response_as_json["product"]["brands"]
            )
            state = "200"
        except Exception as e:
            print(str(e))
            brand = None
            state = "306"
        try:
            Product.objects.create(
                name=response_as_json["product"]["product_name"],
                brand=brand,
                code=code,
                state=state,
                data_source="1",
            )
        except Exception:
            print(str(Exception))
        answer = create_feedback_string(
            request, Product.objects.get(code=code)
        )
        return JsonResponse(answer)
    else:
        print(f"Intial save product with code {code}.")
        Product.objects.create(code=code, state="209")

        params = {"code": code}
        try:
            print(f"sending code {code} to AWS lambda")
            requests.post(
                "https://jr08d16pid.execute-api.eu-central-1.amazonaws.com/prod/",
                params=params,
                timeout=1,
            )
        except Exception as e:
            print(str(e))
            pass
        return HttpResponse(status=209)


def result_feedback(request, code):
    if Product.objects.filter(code=code).exists():
        product_object = Product.objects.get(code=code)
        answer = create_feedback_string(product_object)
        return JsonResponse(answer)
    else:
        return HttpResponse("Not yet in database")


def lookup(code):
    product = scrape(code)
    return product


def local_lookup(request, code):
    scraper = local_scraper(code)
    product = scraper.scrape()
    return product


# TODO: endpoints are not protected with csrf❗️
# in the end it doesnt only save the product but checks for a lot of things
# before hand
@csrf_exempt
def endpoint_save_product(request):
    product = json.loads(request.body.decode("utf-8"))
    if (
        request.method == "POST"
        and Product.objects.filter(code=product["code"]).exists()
    ):
        print(f"Updating product with code: {product['code']}\n")
        brand = None
        if product["brand"] is not None:
            brand, created = Brand.objects.get_or_create(name=product["brand"])
        sub_product_category = None
        if product["sub_product_category"] is not None:
            (
                sub_product_category,
                created,
            ) = SubProductCategory.objects.get_or_create(
                name=product["sub_product_category"]
            )
        product_category = None
        if product["product_category"] is not None:
            product_category, created = ProductCategory.objects.get_or_create(
                name=product["product_category"]
            )
        main_product_category = None
        if product["main_product_category"] is not None:
            (
                main_product_category,
                created,
            ) = MainProductCategory.objects.get_or_create(
                name=product["main_product_category"]
            )
        Product.objects.filter(code=product["code"]).update(
            name=product["name"],
            brand=brand,
            main_product_category=main_product_category,
            product_category=product_category,
            sub_product_category=sub_product_category,
            state=product["state"],
            scraped_image=product["scraped_image"],
        )
    elif request.method == "GET":
        print(f"\nRecieving product to save, code: {product['code']}\n")
        product_obj = Product(code=product["code"], state=product["state"],)
        product_obj.save()
    else:
        print("Something went wrong❗️")
    return HttpResponse("")


@csrf_exempt
def endpoint_update_product(request):
    if request.method == "POST":
        json_product = json.loads(request.body.decode("utf-8"))
        product = Product.objects.get(code=json_product["code"])
        try:
            product.name = json_product["name"]
        except Exception as e:
            print("name n.a.", str(e))
        try:
            product.brand, created = Brand.objects.get_or_create(
                name=json_product["brand"]
            )
        except Exception as e:
            print("brand n.a.", str(e))
        try:
            (
                product.main_product_category,
                created,
            ) = MainProductCategory.objects.get_or_create(
                name=json_product["category"]
            )
        except Exception as e:
            print("category n.a.", str(e))
        product.state = "211"
        product.save()
        return JsonResponse(json_product)


@csrf_exempt
def endpoint_save_brand(request):
    # checking if it is POST could also be outsourced because it is the same in
    # everyfunction
    if request.method == "POST":
        # can be seperate function
        response = json.loads(request.body.decode("utf-8"))
        Corporation.objects.get_or_create(name=response["corporation"])
        # function should start with try except
        try:
            # this is the actual function according to the name
            Brand.objects.get_or_create(
                name=response["name"],
                corporation=Corporation.objects.get(
                    name=response["corporation"]
                ),
            )
        except Exception as e:
            print(
                "\n ERROR while Saving Brand:",
                str(e),
                f"\nBrand Name: {response['name']}\nLength Brand name: {len(response['name'])}\n",
            )
    # why empty http presponse
    return HttpResponse("")


@csrf_exempt
def endpoint_save_company(request):
    # checking if it is POST could also be outsourced because it is the same in
    # everyfunction
    if request.method == "POST":
        # duplicatd can be own function
        response = json.loads(request.body.decode("utf-8"))
        # is not referred to in function name
        Corporation.objects.get_or_create(name=response["corporation"])

        Company.objects.get_or_create(
            name=response["name"],
            corporation=Corporation.objects.get(name=response["corporation"],),
        )
    # why empty http presponse
    return HttpResponse("")


# Actually creates Corporation and Company
@csrf_exempt
def endpoint_save_corporation(request):
    # checking if it is POST could also be outsourced because it is the same in
    # everyfunction
    if request.method == "POST":
        # duplicatd can be own function
        response = json.loads(request.body.decode("utf-8"))
        Corporation.objects.get_or_create(name=response["corporation"])
    # why empty http presponse
    return HttpResponse("")


@csrf_exempt
def endpoint_save_country(request):
    # checking if it is POST could also be outsourced because it is the same in
    # everyfunction
    if request.method == "POST":
        # duplicatd can be own function

        response = json.loads(request.body.decode("utf-8"))
        country_code = None
        try:
            country_code = json.loads(
                requests.get(
                    f"https://restcountries.eu/rest/v2/name/{response['name']}"
                ).content
            )
            if country_code["status"] != 404:
                country_code = country_code[0]["alpha2Code"]
            else:
                country_code = None
        except Exception:
            print(str(Exception), "Can't find country (code).")
        Country.objects.get_or_create(name=response["name"], code=country_code)
    return HttpResponse("")


@csrf_exempt
def current_categories(request):
    if request.method == "GET":
        current_categories = list(MainProductCategory.objects.values())
        return JsonResponse(current_categories, safe=False)


def product_validation(request):
    if request.method == "POST":
        response = json.loads(request.body.decode("utf-8"))
        code = response["barcode"]
        upvote_counter = response["upvote-counter"]
        downvote_counter = response["downvote-counter"]
        product_object = Product.objects.get(code=code)
        if upvote_counter:
            product_object.upvote_counter += 1
        elif downvote_counter:
            product_object.downvote_counter += 1
        product_object.save()
        return HttpResponse("")
