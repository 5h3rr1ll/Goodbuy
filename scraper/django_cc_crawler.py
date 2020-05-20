import os

from django.core import serializers
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from goodbuyDatabase.models import (
    Brand,
    MainProductCategory,
    Product,
    ProductCategory,
    SubProductCategory,
)


class Scraper:
    def __init__(self, code):
        print(f"Starting scraper for {code}")
        self.product = Product(code=code, state="209")
        self.product.save()
        print(f"Initiate scraper window")
        options = Options()
        options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("user-agent=Anon")
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(
            executable_path=str(os.environ.get("CHROMEDRIVER_PATH")),
            chrome_options=options,
        )
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1200, 1134)
        self.driver.get("https://codecheck.info")

    def scrape(self):
        print("\nSearch for search field...")
        try:
            search_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "search-query"))
            )
            search_field.clear()
            search_field.send_keys(f"{self.product.code}")
            print(" Search field found.")
        except Exception as e:
            print("  Search field ERROR:", str(e))

        print("\nSearch for search button...")
        try:
            search_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "search-submit"))
            )
            search_button.click()
            print(" Button clicked.")
        except Exception as e:
            print("  Search submit button ERROR:", str(e))

        print("\nSearch for product name and categories...")
        try:
            div = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "bc"))
            )
            spans = div.find_elements_by_class_name("bcd")

            if len(spans) >= 3:
                breadcrumbs = []
                for breadcrumb in spans:
                    breadcrumbs.append(breadcrumb.text)
                self.product.main_product_category = MainProductCategory.objects.get_or_create(
                    name=breadcrumbs[1]
                )[
                    0
                ]
                self.product.product_category = ProductCategory.objects.get_or_create(
                    name=breadcrumbs[2]
                )[
                    0
                ]
                self.product.sub_product_category = SubProductCategory.objects.get_or_create(
                    name=breadcrumbs[-1]
                )[
                    0
                ]
                breadcrumb_string = div.text.split(
                    f"{breadcrumbs[-2] + ' ' + breadcrumbs[-1]}"
                )
                self.product.name = breadcrumb_string[-1].strip()
                print(
                    f"""
                    Product name: {self.product.name}
                    Product Category: {self.product.product_category}
                    Sub-Product Category: {self.product.sub_product_category}
                    """
                )
            elif len(spans) == 1:
                self.product.name = (
                    WebDriverWait(self.driver, 10)
                    .until(
                        EC.presence_of_element_located(
                            (By.XPATH, '//*[@id="t-1263277"]')
                        )
                    )
                    .text
                )
                print(f"  Product name: {self.product.name}")
            else:
                print("\nStill something wrong here!\n")
        except Exception as e:
            print(str(e))
            self.product.state = "306"
            product_obj_as_json = serializers.serialize(
                "json", Product.objects.filter(code=self.product.code)
            )
            return HttpResponse(
                product_obj_as_json, content_type="text/json-comment-filtered"
            )

        print("\nSearch for product image...")
        try:
            try:
                no_image = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, ".no-image")
                    )
                )
                print("no-image but doesn't throw error")
            except Exception:
                self.product.scraped_image = (
                    WebDriverWait(self.driver, 10)
                    .until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, ".nf > img")
                        )
                    )
                    .get_attribute("src")
                )
                try:
                    on_error = (
                        WebDriverWait(self.driver, 10)
                        .until(
                            EC.presence_of_element_located(
                                (By.CSS_SELECTOR, ".nf > img")
                            )
                        )
                        .get_attribute("onerror")
                    )
                except Exception:
                    print("No image, Picture", str(Exception))
                print(f" Product image found at {self.product['name']}.")
        except Exception as e:
            print("  Product image ERROR:", str(e))

        print("\nFind more product details div")
        try:
            more_product_detail_div = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(text(), 'Mehr Infos')]")
                )
            )
            more_product_detail_div.click()
        except Exception as e:
            print("  More Product Details Div not found:", str(e))

        print("\nInterate over product info items to find product brand...")
        try:
            product_info_items = self.driver.find_elements_by_class_name(
                "product-info-item"
            )

            for div in product_info_items:
                print("\n Text:", div.text)
                if div.text.splitlines()[0] == "Marke":
                    self.product.brand = Brand.objects.get_or_create(
                        name=div.text.splitlines()[1]
                    )[0]
                    print(f"\nBrand Print: {self.product.brand}\n")
            print(f" Product brand is {self.product.brand}.")
        except Exception as e:
            self.product.state = "306"
            print(
                "  Can't extract brand:",
                str(e),
                Brand.objects.get_or_create(name=div.text.splitlines()[1])[0],
            )
            return HttpResponse(status=306)
        print(f"\nName: {self.product.name} Brand: {self.product.brand}\n")

        if self.product.name is not None and self.product.brand is not None:
            self.product.state = "200"
            self.product.data_source = "2"
            print("✅ Looked up product: ", self.product)
        else:
            self.product.state = "306"
            print("Name and/or brand is None")
        self.product.save()
        self.driver.quit()
        product_obj_as_json = serializers.serialize(
            "json", Product.objects.filter(code=self.product.code)
        )
        return HttpResponse(
            product_obj_as_json, content_type="text/json-comment-filtered"
        )
