from django.test import TestCase
from goodbuyDatabase.models import Country, Store, Corporation, Rating, Company, Brand


class TestFeedback(TestCase):
    def setUp(self):
        self.product_object = Product()

    def if_product_is_in_progress(self):
        product = Product(state="209")
        self.assertEqual()
