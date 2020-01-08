from django.test import TestCase
import requests
import json


class Lookup(TestCase):
    def test_if_codecheck_is_available(self):
        response = requests.get("https://www.codecheck.info/")
        self.assertEqual(response.status_code, 200)

    # def test_if_lookup_returns_right_product(self):
    #     result = requests.get("http://localhost:8000/lookup/42113539")
    #     expected_product = {
    #         "code": "42113539",
    #         "name": "Big Red (Wrigley\u00b4s)",
    #         "brand": "Big Red",
    #         "product_sub_category": "Kaugummi & Kaudragees",
    #         "scraped_image": "https://cdn.codecheck.info/image/prod/0018/6172/186172_regular.jpg",
    #     }
    #     result_as_dict = json.loads(result.body.decode("utf-8"))
    #     self.assertEqual(result_as_dict, expected_product)
