#!/usr/bin/python3
# *_* coding: utf-8 *_*

"""
This test module tests the endpoints of this application.
"""

from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import RequestFactory
from goodbuyDatabase.endpoints import endpoint_save_product, create_feedback_string
from goodbuyDatabase.models import Product


class TestEndpoints(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="admin", password="Nix123456")
        Product.objects.create(code=54321)
        self.mars = Product.objects.create(name="Mars", code="11111")

    def test_save_product_endpoint(self):
        snickers = {"name": "Snickers", "code": "54321", "brand": "Snocker Inc."}
        request = self.factory.post(
            "/admin/goodbuyDatabase/product",
            data=snickers,
            content_type="application/json",
        )
        request.user = self.user
        endpoint_save_product(request)
        print("Exists? ", Product.objects.filter(code="54321").exists())
        product = Product.objects.get(code="54321")
        self.assertEqual(product.name, "Snickers")

        def test_create_feedback_string(self):
            response = create_feedback_string()
            self.assertEqual(response, self.mars)
