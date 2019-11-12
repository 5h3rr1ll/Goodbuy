import requests
from bs4 import BeautifulSoup

import re

class PepsiCoWikiScraper:
    def __init__(self):
        self.url = "https://en.wikipedia.org/wiki/List_of_assets_owned_by_PepsiCo"
        self.request = requests.get(self.url)
        self.soup = BeautifulSoup(self.request.content, "html.parser")

    def save_brand(self, brand):
        data = {
            "name": brand,
            "corporation": "PepsiCo",
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

    def get_all_categories(self):
        list_of_div_locations = {
            "Trademarks" : "#mw-content-text > div > ul:nth-child(5)",
            "Licensed / Joint Partnership Trademarks": "#mw-content-text > div > ul:nth-child(7)",
            "Breakfast Bars" : "#mw-content-text > div > ul:nth-child(9) > li:nth-child(1) > ul",
            "Coffee Drinks" : "#mw-content-text > div > ul:nth-child(9) > li:nth-child(2) > ul",
            "Energy Drinks" : "#mw-content-text > div > ul:nth-child(9) > li:nth-child(3) > ul",
            "Cereal" : "#mw-content-text > div > ul:nth-child(9) > li:nth-child(4) > ul",
            "Other" : "#mw-content-text > div > ul:nth-child(9) > li:nth-child(5) > ul",
            "Rice Snacks" : "#mw-content-text > div > ul:nth-child(9) > li:nth-child(6) > ul",
            "Side Dishes" : "#mw-content-text > div > ul:nth-child(9) > li:nth-child(7) > ul",
            "Snacks" : "#mw-content-text > div > ul:nth-child(9) > li:nth-child(8) > ul",
            "Soft Drinks (original Pepsi brands)" : "#mw-content-text > div > ul:nth-child(9) > li:nth-child(9) > ul",
            "Sports Nutrition" : "#mw-content-text > div > ul:nth-child(9) > li:nth-child(10) > ul",
            "Bottled Water" : "#mw-content-text > div > ul:nth-child(9) > li:nth-child(11) > ul",
        }
        for category, div_location in list_of_div_locations.items():
            print(f"\nCategory: {category}")
            self.get_rid_of(self.soup.select_one(div_location))


pepsico_wiki = PepsiCoWikiScraper()
pepsico_wiki.get_all_categories()
