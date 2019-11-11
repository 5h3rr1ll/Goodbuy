import requests
from bs4 import BeautifulSoup

import re


class CocaColaWikiScraper:
    def __init__(self):
        self.url = "https://en.wikipedia.org/wiki/List_of_Coca-Cola_brands"
        self.request = requests.get(self.url)
        self.soup = BeautifulSoup(self.request.content, "html.parser")

    def save_brand(self, brand):
        data = {
            "name": brand,
            "corporation": "Coca-Cola",
        }
        requests.post(
            "http://localhost:8000/goodbuyDatabase/save_brand/", json=data,
        )

    def get_rid_of(self, bs_object):
        for list_element in bs_object.findAll("li"):
            link_text = list_element.get_text()
            special_char = re.findall("[\][–)(]", link_text)
            try:
                print(link_text.split(special_char[0])[0])
                self.save_brand(link_text.split(special_char[0])[0].strip())
            except:
                print(link_text)
                self.save_brand(link_text.strip())

    def get_all_products(self):
        list_of_div_locations = {
            "A": "#mw-content-text > div > div:nth-child(5)",
            "B": "#mw-content-text > div > div:nth-child(8)",
            "C": "#mw-content-text > div > div:nth-child(10)",
            "D": "#mw-content-text > div > div:nth-child(12)",
            "E": "#mw-content-text > div > div:nth-child(14)",
            "F": "#mw-content-text > div > div:nth-child(16)",
            "G": "#mw-content-text > div > div:nth-child(18)",
            "H": "#mw-content-text > div > div:nth-child(20)",
            "I": "#mw-content-text > div > div:nth-child(22)",
            "J": "#mw-content-text > div > div:nth-child(24)",
            "K": "#mw-content-text > div > div:nth-child(26)",
            "L": "#mw-content-text > div > div:nth-child(28)",
            "M": "#mw-content-text > div > div:nth-child(30)",
            "N": "#mw-content-text > div > div:nth-child(32)",
            "O": "#mw-content-text > div > div:nth-child(34)",
            "P": "#mw-content-text > div > div:nth-child(36)",
            "Q": "#mw-content-text > div > div:nth-child(38)",
            "R": "#mw-content-text > div > div:nth-child(40)",
            "S": "#mw-content-text > div > div:nth-child(42)",
            "T": "#mw-content-text > div > div:nth-child(44)",
            "U": "#mw-content-text > div > div:nth-child(46)",
            "V": "#mw-content-text > div > div:nth-child(48)",
            "W": "#mw-content-text > div > div:nth-child(50)",
            "Y": "#mw-content-text > div > div:nth-child(52)",
            "Z": "#mw-content-text > div > div:nth-child(54)",
        }
        for start_letter, div_location in list_of_div_locations.items():
            print(f"\nBrands starting with: {start_letter}")
            self.get_rid_of(self.soup.select_one(div_location))


coca_wiki = CocaColaWikiScraper()
coca_wiki.get_all_products()
