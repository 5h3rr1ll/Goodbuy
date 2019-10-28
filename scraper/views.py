from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from django.http import JsonResponse
from django.urls import reverse

from time import sleep
import sys


def scrape(request, code):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(executable_path=r"/Users/ajs/Developer/Goodbuy/scraper/chromedriver", options=chrome_options)
    driver.set_window_position(0, 0)
    driver.set_window_size(1200, 1134)
    driver.get("https://codecheck.info")

    print("\n search field")
    try:
        search_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search-query"))
        )
        search_field.clear()
        search_field.send_keys(f"{code}")
    except Exception as e:
        print("\nsearch field ERROR:", str(e))

    print("\n search button")
    try:
        search_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search-submit"))
        )
        search_button.click()
    except Exception as e:
        print("\n Search submit button ERROR:", str(e))

    print("\n product name")
    try:
        product_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[5]/div[2]/div/h1"))
        )
    except Exception as e:
        print("\n Productname ERROR:", str(e))

    print("\n product image")
    try:
        product_image = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[6]/div[1]/div[1]/div[1]/span/div/img"))
        )
    except Exception as e:
        print("\n Product image ERROR:", str(e))

    print("\n product category")
    try:
        product_category = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[6]/div[1]/div[2]/div/div[1]/p[2]/a"))
        )
    except Exception as e:
        print("\n Product category ERROR:", str(e))

    print("\n more product details div")
    try:
        more_product_detail_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Mehr Infos')]"))
        )
        more_product_detail_div.click()
    except Exception as e:
        print("\n More Product Details Div not found:", str(e))

    print("\n interate over product info items")
    sleep(3)
    try:
        product_info_items = driver.find_elements_by_class_name("product-info-item")
        for div in product_info_items:
            print("\n Text:", div.text)
            if div.text.splitlines()[0] == "Marke" or div.text.splitlines()[0] == "Marke":
                product_brand = div.text.splitlines()[1]
    except Exception as e:
        print("\n Can't extract brand:", str(e))
        return redirect(f"/goodbuyDatabase/add/product/{code}")

    print("Product is done")
    product = {
        "code" : code,
        "product_name" : product_name.text,
        "brand" : product_brand,
        "product_category" : product_category.text,
        "product_image" : product_image.get_attribute("src"),
    }
    print("Product: ", product)

    return JsonResponse(product)
