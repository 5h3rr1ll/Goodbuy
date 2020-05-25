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
from .selenium_chrome_options import options
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


# Single Responsibility Principle (SRP), Good identifier names, Error handling
# and Exceptions
class CodeCheckScraper:
    def __init__(self, code):
        self.product = Product(code=code, state="209", data_source="2")
        self.product.save()
        self.driver = webdriver.Chrome(
            executable_path=str(os.environ.get("CHROMEDRIVER_PATH")),
            chrome_options=options(),
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
        self.search_product_on_cc()

    def search_product_on_cc(self):
        search_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "search-submit"))
        )
        search_button.click()
        self.find_product_name()

    def get_breadcrum_span_with_categories_and_name(self):
        breadcrums_span = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "bc"))
        )
        list_of_breadcrums = breadcrums_span.find_elements_by_class_name("bcd")
        return breadcrums_span, list_of_breadcrums

    def find_product_name(self):
        (
            breadcrums_span,
            list_of_breadcrums,
        ) = self.get_breadcrum_span_with_categories_and_name()
        if len(list_of_breadcrums) >= 3:
            self.get_product_categories_and_name(breadcrums_span, list_of_breadcrums)
        elif len(list_of_breadcrums) == 1:
            self.get_product_name()

    def get_product_categories_and_name(self, breadcrums_span, list_of_breadcrums):
        """
        This function is taken, if the div filters the product name out of the
        breadcrumb div, since the product name can consists out of serveral
        parts, it's at the moment necessary to do it within this step.
        """
        breadcrumbs = [breadcrumb.text for breadcrumb in list_of_breadcrums]
        self.product.main_product_category = MainProductCategory.objects.get_or_create(
            name=breadcrumbs[1]
        )[0]
        self.product.product_category = ProductCategory.objects.get_or_create(
            name=breadcrumbs[2]
        )[0]
        self.product.sub_product_category = SubProductCategory.objects.get_or_create(
            name=breadcrumbs[-1]
        )[0]
        print("Breadcrums Span: ", breadcrums_span.text)
        breadcrumb_string = breadcrums_span.text.split(
            f"{breadcrumbs[-2] + ' ' + breadcrumbs[-1]}"
        )
        print("BreadCrum String: ", breadcrumb_string)
        self.product.name = breadcrumb_string[-1].strip()
        self.find_product_image()

    def get_product_name(self):
        self.product.name = (
            WebDriverWait(self.driver, 10)
            .until(EC.presence_of_element_located((By.ID, '//*[@id="t-1263277"]')))
            .text
        )
        self.find_product_image()

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
        self.get_and_click_more_product_details_div()

    def get_and_click_more_product_details_div(self):
        more_product_detail_div = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Mehr Infos')]")
            )
        )
        more_product_detail_div.click()
        self.wait_for_product_details_div()

    def wait_for_product_details_div(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Weniger Infos')]")
            )
        )
        self.get_product_brand()

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
        self.check_product_completeness()

    def check_product_completeness(self):
        self.product.state = "200"
        important_attr = ["name", "brand_id"]
        for attr, value in self.product.__dict__.items():
            if attr in important_attr and value is None:
                self.product.state = "306"

    def scrape(self):
        self.find_search_field_and_pass_product_code()
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
