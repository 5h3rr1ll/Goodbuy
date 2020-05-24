#!/usr/bin/python3
# *_* coding: utf-8 *_*

"""
This module is a scraper, useing selenium, to gather informations about a
certain product.
"""

import os

from django.forms.models import model_to_dict
from django.http import JsonResponse
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


class CodeCheckScraper:
    def __init__(self, code):
        self.product = Product(code=code, state="209", data_source="2")
        self.product.save()
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

    def find_search_field_and_pass_product_code(self):
        search_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "search-query"))
        )
        search_field.clear()
        search_field.send_keys(f"{self.product.code}")
        return search_field

    def search_product_on_cc(self):
        search_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "search-submit"))
        )
        search_button.click()
        return search_button

    def get_breadcrum_div(self):
        div = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "bc"))
        )
        span = div.find_elements_by_class_name("bcd")
        return div, span

    def get_product_categories_and_name(self):
        """
        This function is taken, if the div filters the product name out of the
        breadcrumb div, since the product name can consists out of serveral
        parts, it's at the moment necessary to do it within this step.
        """
        div, span = self.get_breadcrum_div()
        breadcrumbs = [breadcrumb.text for breadcrumb in span]
        self.product.main_product_category = MainProductCategory.objects.get_or_create(
            name=breadcrumbs[1]
        )[0]
        self.product.product_category = ProductCategory.objects.get_or_create(
            name=breadcrumbs[2]
        )[0]
        self.product.sub_product_category = SubProductCategory.objects.get_or_create(
            name=breadcrumbs[-1]
        )[0]
        breadcrumb_string = div.text.split(f"{breadcrumbs[-2] + ' ' + breadcrumbs[-1]}")
        self.product.name = breadcrumb_string[-1].strip()
        return (
            self.product.name,
            self.product.main_product_category,
            self.product.product_category,
            self.product.sub_product_category,
        )

    def get_product_name(self):
        self.product.name = (
            WebDriverWait(self.driver, 10)
            .until(EC.presence_of_element_located((By.ID, '//*[@id="t-1263277"]')))
            .text
        )
        return self.product.name

    def find_product_name(self):
        div, span = self.get_breadcrum_div()
        if len(span) >= 3:
            self.get_product_categories_and_name()
        elif len(span) == 1:
            self.get_product_name()

    def find_product_image(self):
        try:
            no_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".no-image"))
            )
        except Exception:
            self.product.scraped_image = (
                WebDriverWait(self.driver, 10)
                .until(EC.presence_of_element_located((By.CSS_SELECTOR, ".nf > img")))
                .get_attribute("src")
            )
            try:
                on_error = (
                    WebDriverWait(self.driver, 10)
                    .until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, ".nf > img"))
                    )
                    .get_attribute("onerror")
                )
            except Exception:
                print("No image, Picture", str(Exception))

    def get_and_click_more_product_details_div(self):
        more_product_detail_div = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Mehr Infos')]")
            )
        )
        more_product_detail_div.click()

    def wait_for_product_details_div(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Weniger Infos')]")
            )
        )

    def get_product_brand(self):
        try:
            product_info_items = self.driver.find_elements_by_class_name(
                "product-info-item"
            )
            for div in product_info_items:
                if div.text.splitlines()[0] == "Marke":
                    self.product.brand = Brand.objects.get_or_create(
                        name=div.text.splitlines()[1]
                    )[0]
        except Exception as e:
            print(str(e))

    def check_product_completeness(self):
        self.product.state = "200"
        important_attr = ["name", "brand_id"]
        for attr, value in self.product.__dict__.items():
            if attr in important_attr and value is None:
                self.product.state = "306"

    def scrape(self):
        self.find_search_field_and_pass_product_code()
        self.search_product_on_cc()
        self.find_product_name()
        self.find_product_image()
        self.get_and_click_more_product_details_div()
        self.wait_for_product_details_div()
        self.get_product_brand()
        self.check_product_completeness()
        self.product.save()
        self.driver.quit()
        return JsonResponse(
            model_to_dict(
                self.product,
                fields=[
                    "name",
                    "code",
                    "brand",
                    "main_product_category",
                    "product_category",
                    "sub_product_category",
                    "state",
                ],
            )
        )
