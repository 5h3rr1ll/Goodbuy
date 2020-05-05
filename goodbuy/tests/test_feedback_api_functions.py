# from unittest import TestCase
# import requests
# from goodbuyDatabase.models import Corporation, Product
#
#
# class TestFeedbackApiFunctions(TestCase):
#
#     def setUp(self):
#         self.ean_code_in_db = '2000423339488'
#         self.ean_code_not_in_db = '4000582185399'
#
#         self.corporation_obj = Corporation.objects.get_or_create(
#             name='Coca-Cola'
#         )
#         self.corporation_obj_not_in_big_ten = Corporation.objects.get_or_create(
#             name='Twix'
#         )
#         self.product_obj = Product.objects.get_or_create(
#             code=self.ean_code_in_db,
#             corporation=Corporation.objects.get(name='Coca-Cola')
#         )
#         self.product_obj_not_in_big_ten = Product.objects.get_or_create(
#             code=self.ean_code_not_in_db,
#             corporation=Corporation.objects.get(name='Twix')
#         )
#     def test_corporation_of_product_is_in_big_ten(self):
#         response = requests.get(f'http://127.0.0.1:8000/is_big_ten/{self.ean_code_in_db}/')
#         print(response.status_code)
#         self.assertEqual(response.text, 'True')
#
#
#     def test_corporation_of_product_is_not_in_database(self):
#         response = requests.get(f'http://127.0.0.1:8000/is_big_ten/1984781927381/')
#         print(response.status_code)
#         self.assertEqual(response.text, 'We don\'t know')
#
#
#     def test_corportation_of_product_is_not_in_big_ten(self):
#         response = requests.get(f'http://127.0.0.1:8000/is_big_ten/{self.ean_code_not_in_db}/')
#         print(response.status_code)
#         self.assertEqual(response.text, 'False')
