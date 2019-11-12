import requests
from bs4 import BeautifulSoup

import re


class UnileverWikiScraper:
    def __init__(self):
        self.url = "https://en.wikipedia.org/wiki/List_of_Unilever_brands"
        self.request = requests.get(self.url)
        self.soup = BeautifulSoup(self.request.content, "html.parser")

    def save_brand(self, brand):
        data = {
            "name": brand,
            "corporation": "Unilever",
        }
        requests.post(
            "http://localhost:8000/goodbuyDatabase/save_brand/", json=data,
        )

    def get_rid_of(self, bs_object):
        for list_element in bs_object.findAll("li"):
            link_text = list_element.get_text()
            special_char = re.findall("[\][–)(,}:]|[0-9]{4}", link_text)
            try:
                print(link_text.split(special_char[0])[0])
                self.save_brand(link_text.split(special_char[0])[0].strip())
            except:
                print(link_text)
                self.save_brand(link_text.strip())

    def get_all_products(self):
        list_of_div_locations = {
            "Billion-euro per Year" : "#mw-content-text > div > div:nth-child(5)",
            "Food and beverages" : "#mw-content-text > div > div:nth-child(7)",
            "Home care and beauty & personal care brands" : "#mw-content-text > div > div:nth-child(23)",
        }
        for Category, div_location in list_of_div_locations.items():
            print(f"\nBrands starting with: {Category}")
            self.get_rid_of(self.soup.select_one(div_location))


unilever_wiki = UnileverWikiScraper()
unilever_wiki.get_all_products()