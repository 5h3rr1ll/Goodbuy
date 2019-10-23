from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from django.http import HttpResponse
from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from django.http import JsonResponse

import time
import sys


# Create your views here.
def scrape(request, code):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(executable_path=r"/Users/ajs/Developer/Goodbuy/scraper/chromedriver", options=chrome_options)
    # driver.set_window_position(0, 0)
    driver.set_window_size(1200, 1134)
    driver.get("https://codecheck.info")

    try:
        search_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search-query"))
        )
        search_field.clear()
        search_field.send_keys("{}".format(code))
    except Exception as e:
        print("\nsearch field ERROR:", str(e))

    try:
        search_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search-submit"))
        )
        search_button.click()
    except Exception as e:
        print("\nsearch-submit-button field ERROR:", str(e))

    try:
        product_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[5]/div[2]/div/h1"))
        )
    except Exception as e:
        print("\n Productname ERROR:", str(e))

    try:
        product_category = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[6]/div[1]/div[2]/div/div[1]/p[2]/a"))
        )
    except Exception as e:
        print("\n Product category ERROR:", str(e))

    try:
        more_product_detail_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[6]/div[1]/div[2]/div/div[7]"))
        )
        more_product_detail_button.click()
    except Exception as e:
        print("\n More Product Details ERROR:", str(e))

    try:
        product_brand = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[6]/div[1]/div[2]/div/div[6]/div[5]/p[2]/a"))
        )
    except Exception as e:
        print("\n Brand ERROR:", str(e))

    product = {
        "code" : code,
        "product_name" : product_name.text,
        "brand" : product_brand.text,
        "product_category" : product_category.text
    }

    return JsonResponse(product)
