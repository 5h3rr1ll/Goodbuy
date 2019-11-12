from django.test import TestCase
import requests, json

class CodeCheck(TestCase):

    def setUp(self):
        pass

    def test_if_code_check_returns_right_product(self):
        result = requests.get('http://localhost:8000/lookup/42113539')
        expected_product = str({"code": "42113539", "name": "Big Red (Wrigleys)", "brand": "Big Red", "product_category": "Kaugummi & Kaudragees", "scraped_image": "https://cdn.codecheck.info/image/prod/0018/6172/186172_regular.jpg"})
        print(result.text)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(str(result.text), expected_product)
