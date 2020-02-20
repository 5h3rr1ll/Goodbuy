import json

import requests
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rq import Queue

from goodbuyDatabase.models import (BigTen, Brand, Company, Corporation,
                                    Country, MainProductCategory, Product,
                                    ProductCategory, SubProductCategory)
from scraper.aws_lambda_cc_crawler import scrape
from scraper.django_cc_crawler import scrape as local_scrape
from worker import conn

q = Queue(connection=conn)


def is_in_own_database(request, code):
    return HttpResponse(str(Product.objects.filter(code=code).exists()))


def is_big_ten(request, code):
    if Product.objects.get(code=code).brand is None:
        return "We don't know"
    brand = Brand.objects.filter(name__trigram_similar=Product.objects.get(code=code).brand)[0]
    return BigTen.objects.filter(name__trigram_similar=brand.name).exists()


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
    brand, corporation, sub_product_category = check_for_attributes(request, product_object)
    product_serialized = serializers.serialize("json", [product_object, ])
    product_serialized = product_serialized.strip("[]")
    product_serialized = json.loads(product_serialized)
    product_serialized["fields"]["brand"] = brand
    product_serialized["fields"]["corporation"] = corporation
    product_serialized["fields"]["sub_product_category"] = sub_product_category
    # Checks if it is big ten
    is_big_ten_answer = is_big_ten(request, code=product_object.code)
    product_serialized["is_big_ten"] = is_big_ten_answer
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
        answer = create_feedback_string(request, Product.objects.get(code=code))
        return JsonResponse(answer)
    else:
        print(f"Intial save product with code {code}.")
        Product.objects.create(code=code, state="209")

        params = {"code": code}
        try:
            print(f"sending code {code} to AWS lambda")
            requests.post(
                "https://4vyxihyubj.execute-api.eu-central-1.amazonaws.com/dev/",
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


def lookup(request, code):
    product = scrape(code)
    return product


def local_lookup(request, code):
    product = local_scrape(code)
    return product

# TODO: endpoints are not protected with csrf❗️
# in the end it doesnt only save the product but checks for a lot of things before hand
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
            sub_product_category, created = SubProductCategory.objects.get_or_create(
                name=product["sub_product_category"]
            )
        product_category = None
        if product["product_category"] is not None:
            product_category, created = ProductCategory.objects.get_or_create(
                name=product["product_category"]
            )
        main_product_category = None
        if product["main_product_category"] is not None:
            main_product_category, created = MainProductCategory.objects.get_or_create(
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
    return HttpResponse("")


@csrf_exempt
def endpoint_save_brand(request):
    # checking if it is POST could also be outsourced because it is the same in everyfunction
    if request.method == "POST":
        # can be seperate function
        response = json.loads(request.body.decode("utf-8"))
        Corporation.objects.get_or_create(name=response["corporation"])
        # function should start with try except
        try:
            # this is the actual function according to the name
            Brand.objects.get_or_create(
                name=response["name"],
                corporation=Corporation.objects.get(name=response["corporation"]),
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
    # checking if it is POST could also be outsourced because it is the same in everyfunction
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
    # checking if it is POST could also be outsourced because it is the same in everyfunction
    if request.method == "POST":
        # duplicatd can be own function
        response = json.loads(request.body.decode("utf-8"))
        Corporation.objects.get_or_create(name=response["corporation"])
    # why empty http presponse
    return HttpResponse("")


@csrf_exempt
def endpoint_save_country(request):
    # checking if it is POST could also be outsourced because it is the same in everyfunction
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
