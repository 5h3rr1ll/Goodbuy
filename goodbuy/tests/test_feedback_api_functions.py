from unittest import TestCase
import nose
import requests

from goodbuyDatabase.models import Brand, Corporation



class TestFeedbackApiFunctions(TestCase):

    def setUp(self):
        nose.main()
        self.ean_code_in_db = '2000423339488'
        self.ean_code_not_in_db = '4000582185399'

        self.corporation_obj = Corporation.objects.create(
            name='Coke'
        )
        self.brand_obj = Brand.objects.create(
            name='Coca-Cola',
            corporation='Coke'
        )

    def test_corporation_of_brand_is_in_big_ten(self):
        response = requests.get('http://127.0.0.1:8000/is_big_ten/Coca%20Cola/')
        self.assertEqual(response.text, True)


    def test_corporation_of_brand_is_not_in_database(self):
        response = requests.get('http://127.0.0.1:8000/is_big_ten/Snickers/')
        self.assertEqual(response.text, 'We don\'t know')


    def test_corportation_of_brand_is_not_in_big_ten(self):
        response = requests.get('http://127.0.0.1:8000/is_big_ten/Schnick/')
        self.assertEqual(response.text, False)
