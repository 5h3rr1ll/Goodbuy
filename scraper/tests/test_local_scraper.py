from django.test import TestCase
from django.urls import reverse

# from scraper.django_cc_crawler import Scraper


class LocalCCScraper(TestCase):
    # def setUp(self):
    #     self.scraper = Scraper("5000112640168")

    # def test_search_field_founded(self):
    #     self.scraper.search_for_product_on_cc()

    def test_return_200(self):
        url = reverse("django_lookup", args=[5000112640168])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
