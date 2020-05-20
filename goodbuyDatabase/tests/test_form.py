from django.test import TestCase
from django.urls import reverse

from goodbuyDatabase.forms import AddNewProductForm


# model test
class GoodbuyDatabaseTest(TestCase):
    def test_valid_form(self):
        data = {"code": "1234567", "name": "Mars"}
        form = AddNewProductForm(data=data)
        self.assertTrue(form.is_valid())

    def test_add_new_product_view(self):
        url = reverse("goodbuyDatabase:add_product_form", args=[123456])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(
            "<title>Add Product</title>", resp.content.decode("utf-8")
        )
