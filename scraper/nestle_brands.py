import os
import re

import requests
from bs4 import BeautifulSoup


class NestleWikiScraper:
    def __init__(self):
        self.url = "https://en.wikipedia.org/wiki/List_of_Nestl%C3%A9_brands"
        self.request = requests.get(self.url)
        self.soup = BeautifulSoup(self.request.content, "html.parser")

    def save_brand(self, brand):
        data = {
            "name": brand,
            "corporation": "Nestlé",
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
            "Beverages": "#mw-content-text > div > div:nth-child(10)",
            "Coffee": "#mw-content-text > div > div:nth-child(12)",
            "Water": "#mw-content-text > div > div:nth-child(14)",
            "Cereals": "#mw-content-text > div > div:nth-child(16)",
            "Chilled": "#mw-content-text > div > div:nth-child(19)",
            "Choclate & Co.": "#mw-content-text > div > div:nth-child(21)",
            "Foodservice products": "#mw-content-text > div > ul:nth-child(23)",
            "Frozen food": "#mw-content-text > div > div:nth-child(25)",
            "Frozen Dessert": "#mw-content-text > div > div:nth-child(27)",
            "Healthcare nutrition": "#mw-content-text > div > div:nth-child(29)",
            "Infant foods": "#mw-content-text > div > div:nth-child(31)",
            "Performance nutrition": "#mw-content-text > div > ul:nth-child(33)",
            "Petcare": "#mw-content-text > div > div:nth-child(35)",
            "Purina petcare products": "#mw-content-text > div > div:nth-child(38)",
            "Refrigerated products": "#mw-content-text > div > ul:nth-child(40)",
            "Seasonings": "#mw-content-text > div > ul:nth-child(43)",
            "Shelf stable": "#mw-content-text > div > ul:nth-child(45)",
            "Yogurt": "#mw-content-text > div > div:nth-child(47)",
        }
        return div_locations_list

    def iterate_over_list(self, lst):
        for category, div_location in lst.items():
            print(f"\n{category}:")
            div_location = self.soup.select_one(div_location)
            self.clean_up_brand_name(div_location)


NESTLE_WIKI = NestleWikiScraper()
NESTLE_WIKI.iterate_over_list(NESTLE_WIKI.get_all_div_location())
