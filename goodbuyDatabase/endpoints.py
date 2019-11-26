import json
import os

import requests
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rq import Queue

from goodbuyDatabase.models import (
    Brand,
    CategoryOfProduct,
    Company,
    Corporation,
    Country,
    Product,
)
from scraper.views import scrape
from worker import conn

q = Queue(connection=conn)


def is_big_ten(request, code):
    big_ten = [
        "Unilever",
        "Nestlé",
        "Coca-Cola",
        "Coca Cola",
        "Kellog's",
        "MARS",
        "PepsiCo",
        "Mondelez",
        "General Mills",
        "Associated British Foods",
        "Danone",
    ]
    product_obj = Product.objects.get(code=code)
    if product_obj.brand is None:
        return HttpResponse("We don't know")
    elif product_obj.brand.corporation is None:
        return HttpResponse("False")
    else:
        return HttpResponse(product_obj.brand.corporation.name in big_ten)


def is_in_own_database(code):
    return HttpResponse(str(Product.objects.filter(code=code).exists()))


def check_for_attributes(product_object):
    try:
        brand = product_object.brand.name
    except Exception:
        brand = ""
        print(str(Exception))
    try:
        corporation = product_object.brand.corporation.name
    except Exception:
        corporation = ""
        print(str(Exception))
    try:
        product_category = product_object.product_category.name
    except Exception:
        product_category = ""
        print(str(Exception))
    return(brand, corporation, product_category)


# Creates feedback string but also returns it with the product_object
def create_feedback_string(product_object):
    brand, corporation, product_category = check_for_attributes(product_object)
    product_serialized = serializers.serialize("json", [product_object, ])
    product_serialized = product_serialized.strip("[]")
    product_serialized = json.loads(product_serialized)
    product_serialized['fields']['brand'] = brand
    product_serialized['fields']['corporation'] = corporation
    product_serialized['fields']['product_category'] = product_category
    # Checks if it is big ten
    # Try Except should be own function
    try:
        # why not call is big ten directly?
        is_big_ten = requests.get(
            f"{os.environ.get('CURRENT_HOST')}/is_big_ten/{product_object.code}/"
        ).content.decode("utf-8")
    except Exception as e:
        print("\n request ERROR:", str(e))
    # Here is the actual creation of the string according to the name
    is_big_ten_string = {
        "is_big_ten": is_big_ten,
        "brand": brand,
        "corporation": corporation,
    }
    product_serialized["is_big_ten"] = is_big_ten
    return(product_serialized)


def feedback(request, code):
    # looks if product exist in database
    if Product.objects.filter(
        code=code
    ).exists():  # Does it make sense to call a function instead
        # product exists calls for string creation and then returns json answer
        product_object = Product.objects.get(code=code)
        answer = create_feedback_string(product_object)
        return JsonResponse(answer)
    # product doesnt exist in db so start codecheck scraper
    # save the product in database
    # then get the product out of the database again (?)
    # calls function to build feedback string
    # returns json answer
    else:
        result = q.enqueue(scrape, code, result_ttl=0)
        return HttpResponse(status=209)


def result_feedback(request, code):
    if Product.objects.filter(
        code=code
    ).exists():
        product_object = Product.objects.get(code=code)
        answer = create_feedback_string(product_object)
        return JsonResponse(answer)
    else:
        return HttpResponse("Not yet in database")


def lookup(request, code):
    product = scrape(code)
    return product


# TODO: endpoints are not protected with csrf❗️
# in the end it doesnt only save the product but checks for a lot of things before hand
@csrf_exempt
def endpoint_save_product(request):
    # initializes brand and product_category
    brand = None
    product_category = None
    # check if request method is post
    # checking if it is POST could also be outsourced because it is the same in everyfunction
    if request.method == "POST":
        # loads the response
        # json loading can be a seperate function because this is in all endpoints necessary
        response = json.loads(request.body.decode("utf-8"))
        # checks if brand exists in response could maybe be replaced by N.A initial value and then get or
        # create why is get or create when we check before if it is not none same for product_category
        if response["brand"] is not None:
            brand, created = Brand.objects.get_or_create(name=response["brand"])
        if response["product_category"] is not None:
            product_category, created = CategoryOfProduct.objects.get_or_create(
                name=response["product_category"]
            )
        product_object, created = Product.objects.get_or_create(
            code=response["code"],
            name=response["name"],
            brand=brand,
            product_category=product_category,
            scraped_image=response["scraped_image"],
        )
    # why empty http presponse
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
