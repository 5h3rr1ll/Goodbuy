import requests
from bs4 import BeautifulSoup

import re

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
            "Original products": "#mw-content-text > div > div:nth-child(68)",
            "Products manufactured by The Wrigley Company": "#mw-content-text > div > div:nth-child(70)",
            "Products for pet consumption": "#mw-content-text > div > div:nth-child(72)",
        }
        for category, div_location in list_of_div_locations.items():
            print(f"\nCategory: {category}")
            self.get_rid_of(self.soup.select_one(div_location))


mars_wiki = MarsWikiScraper()
mars_wiki.get_all_categories()
