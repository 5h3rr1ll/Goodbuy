from django.test import LiveServerTestCase, Client
from django.urls import reverse


class TestView(LiveServerTestCase):
    def setup(self):
        self.client = Client()


    # def test_show_list_of_codes(self):
    #     client = Client()
    #     response = client.get(reverse('goodbuyDatabase:show_list_of_codes', args=['4000582185399']))
    #     print(response)
    #     self.assertEqual(response.status_code, 200)
    #     #self.assertTemplateUsed(response, 'goodbuyDatabase/list_of_product_codes.html')

    def test_is_in_own_db(self):
        response = self.client.get(reverse('goodbuyDatabase:is_in_own_database', args=['4000582185399']))
        self.assertEqual(response.status_code, 200)

    # def test_product_list(self):
    #     response = self.client.get(reverse('goodbuyDatabase:product_list'))
    #     self.assertEqual(response.status_code, 200)