from django.test import TestCase
from django.urls import reverse


class LocalCCScraper(TestCase):
    def test_return_200(self):
        url = reverse("django_lookup", args=[5000112640168])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        # self.assertIn(
        #     "<title>Add Product</title>", resp.content.decode("utf-8")
        # )
