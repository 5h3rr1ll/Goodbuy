import os
import re

import requests
from bs4 import BeautifulSoup


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
            f"{os.environ.get('CURRENT_HOST')}/goodbuyDatabase/save_brand/", json=data,
        )

    def clean_up_brand_name(self, bs_object):
        try:
            if bs_object.findAll("li") == []:
                print("empty Error")
            else:
                for list_element in bs_object.findAll("li"):
                    link_text = list_element.get_text()
                    special_char = re.findall(r"[\][–)(,}:]|[0-9]{4}", link_text)
                    try:
                        print(link_text.split(special_char[0])[0])
                        self.save_brand(link_text.split(special_char[0])[0].strip())
                    except Exception:
                        print(link_text)
                        self.save_brand(link_text.strip())
        except AttributeError as e:
            print(str(e), " div changed position ")

    def get_all_div_location(self):
        div_locations_list = {
            "Trademarks": "#mw-content-text > div > ul:nth-child(5)",
            "Licensed / Joint Partnership Trademarks": "#mw-content-text > div > ul:nth-child(7)",
            "Breakfast Bars": "#mw-content-text > div > ul:nth-child(9) > li:nth-child(1) > ul",
            "Coffee Drinks": "#mw-content-text > div > ul:nth-child(9) > li:nth-child(2) > ul",
            "Energy Drinks": "#mw-content-text > div > ul:nth-child(9) > li:nth-child(3) > ul",
            "Cereal": "#mw-content-text > div > ul:nth-child(9) > li:nth-child(4) > ul",
            "Other": "#mw-content-text > div > ul:nth-child(9) > li:nth-child(5) > ul",
            "Rice Snacks": "#mw-content-text > div > ul:nth-child(9) > li:nth-child(6) > ul",
            "Side Dishes": "#mw-content-text > div > ul:nth-child(9) > li:nth-child(7) > ul",
            "Snacks": "#mw-content-text > div > ul:nth-child(9) > li:nth-child(8) > ul",
            "Soft Drinks (original Pepsi brands)": "#mw-content-text > div > ul:nth-child(9) > li:nth-child(9) > ul",
            "Sports Nutrition": "#mw-content-text > div > ul:nth-child(9) > li:nth-child(10) > ul",
            "Bottled Water": "#mw-content-text > div > ul:nth-child(9) > li:nth-child(11) > ul",
        }
        return div_locations_list

    def iterate_over_list(self, lst):
        for category, div_location in lst.items():
            print(f"\n{category}:")
            div_location = self.soup.select_one(div_location)
            self.clean_up_brand_name(div_location)


PEPSICO_WIKI = PepsiCoWikiScraper()
PEPSICO_WIKI.iterate_over_list(PEPSICO_WIKI.get_all_div_location())
