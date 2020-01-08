from unittest import TestCase
import requests
from goodbuyDatabase.models import Brand, Product


class TestFeedbackApiFunctions(TestCase):
    def setUp(self):
        self.ean_code_in_db = "2000423339488"
        self.ean_code_not_in_db = "4000582185399"
        self.brand_in_db = "Coca-Cola"
        self.brand_not_in_db = "Wesa"

        self.brand_obj = Brand.objects.get_or_create(name="Coca-Cola")
        self.brand_obj_not_in_big_ten = Brand.objects.get_or_create(
            name="Twix"
        )
        self.product_obj = Product.objects.get_or_create(
            code=self.ean_code_in_db,
            brand=Brand.objects.get(name="Coca-Cola"),
        )
        self.product_obj_not_in_big_ten = Product.objects.get_or_create(
            code=self.ean_code_not_in_db,
            brand=Brand.objects.get(name="Twix"),
        )

    # def test_brand_of_product_is_in_big_ten(self):
    #     response = requests.get(
    #         f"http://127.0.0.1:8000/is_big_ten/{self.brand_in_db}/"
    #     )
    #     print(f"Response Code: {response.status_code}")
    #     self.assertEqual(response.text, "True")

    # def test_brand_of_product_is_not_in_database(self):
    #     response = requests.get(f"http://127.0.0.1:8000/is_big_ten/1984781927381/")
    #     # print(response.status_code)
    #     self.assertEqual(response.text, "We don't know")

    # def test_corportation_of_product_is_not_in_big_ten(self):
    #     response = requests.get(
    #         f"http://127.0.0.1:8000/is_big_ten/{self.brand_not_in_db}/"
    #     )
    #     # print(response.status_code)
    #     self.assertEqual(response.text, "False")
