import os
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from django.test import TestCase
from django.urls import reverse
from goodbuyDatabase.forms import AddNewProductForm
from goodbuyDatabase.models import Country, Product


class TestLogIn(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(
            executable_path=str(os.environ.get("CHROMEDRIVER_PATH")),
            chrome_options=options,
        )

    def test_signup_chrome(self):
        self.driver.get("http://localhost:8000/login/")
        self.driver.find_element_by_id("id_username").send_keys("Foo")
        self.driver.find_element_by_id("id_password").send_keys("Bar")
        self.driver.find_element_by_id("login-button").click()
        self.assertEqual(
            "http://localhost:8000/login/", self.driver.current_url
        )

    def tearDown(self):
        self.driver.quit


# model test
class GoodbuyDatabaseTest(TestCase):
    def create_country(self, name="Germany"):
        return Country.objects.create(name=name)

    def create_product(self, name="Snickers", code="123456"):
        return Product.objects.create(name=name, code=code)

    def test_create_country(self):
        country = self.create_country()
        self.assertTrue(isinstance(country, Country))
        self.assertEqual(country.__str__(), country.name)

    def test_create_product(self):
        product = self.create_product()
        self.assertTrue(isinstance(product, Product))
        self.assertEqual(product.__str__(), product.name)

    def test_add_new_product_view(self):
        url = reverse("goodbuyDatabase:add_product_form", args=[123456])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(
            "<title>Add Product</title>", resp.content.decode("utf-8")
        )

    def test_valid_form(self):
        data = {"code": "1234567", "name": "Mars"}
        form = AddNewProductForm(data=data)
        self.assertTrue(form.is_valid())
