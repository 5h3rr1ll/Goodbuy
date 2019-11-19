import os

import requests
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def scrape(code):
    options = Options()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(
        executable_path=str(os.environ.get("CHROMEDRIVER_PATH")), chrome_options=options
    )
    driver.set_window_position(0, 0)
    driver.set_window_size(1200, 1134)
    driver.get("https://codecheck.info")

    print("\nSearch for search field...")
    try:
        search_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search-query"))
        )
        search_field.clear()
        search_field.send_keys(f"{code}")
        print(" Search found.")
    except Exception as e:
        print("  Search field ERROR:", str(e))

    print("\nSearch for search button...")
    try:
        search_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search-submit"))
        )
        search_button.click()
        print(" Button clicked.")
    except Exception as e:
        print("  Search submit button ERROR:", str(e))

    print("\nSearch for product name...")
    try:
        product_name = (
            WebDriverWait(driver, 10)
            .until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".page-title-headline > .float-group > h1")
                )
            )
            .text
        )
        print(f" Product name is {product_name}.")
    except Exception as e:
        # TODO: if name is not found, user needs to get redirected to add product form
        print("  Productname ERROR:", str(e))

    print("\nSearch for product image...")
    try:
        product_image = (
            WebDriverWait(driver, 10)
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, ".nf > img")))
            .get_attribute("src")
        )
        print(f" Product image found at {product_image}.")
    except Exception as e:
        print("  Product image ERROR:", str(e))

    product_category = None
    print("\nSearch for product category...")
    try:
        product_category = (
            WebDriverWait(driver, 10)
            .until(
                EC.presence_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        "div.block.prod-basic-info > div > .product-info-item > p:nth-child(2) > a",
                    )
                )
            )
            .text
        )
        print(f" Product category is {product_category}.")
    except Exception as e:
        print("  Product category ERROR:", str(e))

    print("\nFind more product details div")
    try:
        more_product_detail_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Mehr Infos')]")
            )
        )
        more_product_detail_div.click()
    except Exception as e:
        print("  More Product Details Div not found:", str(e))

    print("\nInterate over product info items to find product brand...")

    product_brand = None
    try:
        product_info_items = driver.find_elements_by_class_name("product-info-item")
        for div in product_info_items:
            print("\n Text:", div.text)
            if div.text.splitlines()[0] == "Marke":
                product_brand = div.text.splitlines()[1]
        print(f" Product brand is {product_brand}.")
    except Exception as e:
        print("  Can't extract brand:", str(e))
        # When there is no brand in the scraped object we return the Httpresponse(403).
        # The Api should know that this is a response to redirect the user in Vue to a view for
        # inserting the brand.
        return HttpResponse(403)

    product = {
        "code": code,
        "name": product_name,
        "brand": product_brand,
        "product_category": product_category,
        "scraped_image": product_image,
    }
    print("✅ Looked up product: ", product)
    requests.post(
        f"{os.environ.get('CURRENT_HOST')}/goodbuyDatabase/save_product/", json=product,
    )
    return str(product)
