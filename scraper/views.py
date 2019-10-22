from django.shortcuts import render
from selenium import webdriver
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from django.http import HttpResponse

# Create your views here.
def scrape(request, code):
    driver = webdriver.Chrome(executable_path=r"/Users/ajs/Developer/Goodbuy/scraper/chromedriver")
    # chrome_options.add_argument("--headless")
    driver.set_window_position(0, 0)
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
        sys.exit()

    try:
        search_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search-submit"))
        )
        search_button.click()
    except Exception as e:
        print("\nsearch-submit-button field ERROR:", str(e))
        sys.exit()

    try:
        code = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[5]/div[1]/div[2]/div/div[1]/p[2]"))
        )
        print("\nCODE:",code.text, "\n")
    except Exception as e:
        print("\n find code ERROR:", str(e))
        sys.exit()

    try:
        brand = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[5]/div[1]/div[2]/div/div[3]/div[3]/p[2]/a"))
        )
        brand = brand.text
    except Exception as e:
        print("\n Brand Var ERROR:", str(e))
        sys.exit()
