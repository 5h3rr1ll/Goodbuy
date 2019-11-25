import os
import re

import requests
from bs4 import BeautifulSoup


class UnileverWikiScraper:
    """Returns brands of unilever"""

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
            "Billion-euro per Year": "#mw-content-text > div > div:nth-child(5)",
            "Food and beverages": "#mw-content-text > div > div:nth-child(7)",
            "Home care and beauty & personal care brands": "#mw-content-text > div > div:nth-child(23)",
        }
        return div_locations_list

    def iterate_over_list(self, lst):
        for category, div_location in lst.items():
            print(f"\n{category}:")
            div_location = self.soup.select_one(div_location)
            self.clean_up_brand_name(div_location)


UNILEVER_WIKI = UnileverWikiScraper()
UNILEVER_WIKI.iterate_over_list(UNILEVER_WIKI.get_all_div_location())
