from django.test import TestCase
from django.urls import reverse
import json


class LocalCCScraper(TestCase):
    def test_successfull_scrape(self):
        url = reverse("django_lookup", args=[42113539])
        resp = self.client.get(url)
        resp_as_json = json.loads(resp.content.decode("utf-8"))
        print("Respons as Json:", resp_as_json)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp_as_json["state"], "200")
        self.assertEqual(resp_as_json["name"], "Big Red (Wrigley´s)")
        self.assertEqual(resp_as_json["brand"], 1)
