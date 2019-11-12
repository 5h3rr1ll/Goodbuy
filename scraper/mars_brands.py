import re

import requests
from bs4 import BeautifulSoup


class MarsWikiScraper:
    def __init__(self):
        self.url = "https://en.wikipedia.org/wiki/Mars,_Incorporated"
        self.request = requests.get(self.url)
        self.soup = BeautifulSoup(self.request.content, "html.parser")

    def save_brand(self, brand):
        data = {
            "name": brand,
            "corporation": "Mars",
        }
        requests.post(
            "http://localhost:8000/goodbuyDatabase/save_brand/", json=data,
        )

    def clean_up_brand_name(self, bs_object):
        try:
            if bs_object.findAll("li") == []:
                print("empty Error")
            else:
                for list_element in bs_object.findAll("li"):
                    link_text = list_element.get_text()
                    special_char = re.findall("[\][–)(,}:]|[0-9]{4}", link_text)
                    try:
                        print(link_text.split(special_char[0])[0])
                        self.save_brand(link_text.split(special_char[0])[0].strip())
                    except:
                        print(link_text)
                        self.save_brand(link_text.strip())
        except AttributeError as e:
            print(str(e), " div changed position ")

    def get_all_div_location(self):
        div_locations_list = {
            "Original products": "#mw-content-text > div > div:nth-child(68)",
            "Products manufactured by The Wrigley Company": "#mw-content-text > div > div:nth-child(70)",
            "Products for pet consumption": "#mw-content-text > div > div:nth-child(72)",
        }
        return div_locations_list

    def iterate_over_list(self, lst):
        for category, div_location in lst.items():
            print(f"\nCategory: {category}")
            div_location = self.soup.select_one(div_location)
            self.clean_up_brand_name(div_location)


mars_wiki = MarsWikiScraper()
div_locations_list = mars_wiki.get_all_div_location()
mars_wiki.iterate_over_list(div_locations_list)
