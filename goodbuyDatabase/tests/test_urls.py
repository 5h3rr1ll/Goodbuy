from django.test import TestCase
from django.urls import reverse, resolve
from goodbuyDatabase.endpoints import is_in_own_database
from goodbuyDatabase.views import product_list, show_list_of_codes


class TestUrls(TestCase):
    def test_is_in_own_database(self):
        url = reverse('goodbuyDatabase:is_in_own_database', args=['4000582185399'])
        self.assertEqual(resolve(url).func, is_in_own_database)

    def test_product_list(self):
        url = reverse('goodbuyDatabase:product_list')
        self.assertEqual(resolve(url).func, product_list)

    def test_show_list_of_codes(self):
        url = reverse('goodbuyDatabase:show_list_of_codes', args=['4000582185399'])
        self.assertEqual(resolve(url).func, show_list_of_codes)
