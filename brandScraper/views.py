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
import sys
import os


def scrape(request):
    options = Options()
    # uncommment next line when deplyoing
    # options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    # options.add_argument("--headless")
    # options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--remote-debugging-port=9222')
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(executable_path=str('brandScraper/chromedriver'), chrome_options=options)
    driver.set_window_position(0, 0)
    driver.set_window_size(1200, 1134)
    driver.get("http://product-open-data.com/brand/list-a")
    
    try:
        rows = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "row"))
        )

    except Exception as e:
        print("\nrow ERROR:", str(e))
                
    try:
        link_to_brand = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "section > div:nth-child(1) > a"))
        )
        link_to_brand.click()
    except Exception as e:
        print("\n link to brand ERROR:", str(e))

    try:
        product_info = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.list-header > div > table > tbody"))
        )
    except Exception as e:
        print("\n Productinfo ERROR:", str(e))

    try: 
        product_img = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.list-header > div > table > tbody > tr > td:nth-child(1) > img"))
        )
    except Exception as e:
        print("\n Product image ERROR:", str(e))

    print("Product is done")
    product = {
        'info': product_info.text,
        "scraped_image" : product_img.get_attribute("src"),
    }
    print("Product: ", product)

    return JsonResponse(product)
