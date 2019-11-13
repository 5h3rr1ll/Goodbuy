"""This module gathers information about brands and companies of corperations."""
import re

import requests
from bs4 import BeautifulSoup


class CocaColaWikiScraper:
    """Returns brands of Coca-Cola"""

    def __init__(self):
        self.url = "https://en.wikipedia.org/wiki/List_of_Coca-Cola_brands"
        self.request = requests.get(self.url)
        self.soup = BeautifulSoup(self.request.content, "html.parser")

    @classmethod
    def save_brand(cls, brand):
        """Takes a brand name and saves it with the corporation into the database"""
        data = {
            "name": brand,
            "corporation": "Kellogg's",
        }
        requests.post(
            "http://localhost:8000/goodbuyDatabase/save_brand/", json=data,
        )

    def clean_up_brand_name(self, bs_object):
        """
        Takes a BeautifulSoup object, searches for all links in it, interate through it. searches
        for special characters to remove unneeded text from the link text. In the end the name
        gets handed over to the save_brand function.
        """
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
                        print(str(Exception), link_text)
                        self.save_brand(link_text.strip())
        except AttributeError as e:
            print(str(e), " div changed position ")

    @classmethod
    def get_all_div_location(cls):
        div_locations_list = {
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
        return div_locations_list

    def iterate_over_list(self, lst):
        """
        Iterates over the list of div locations. Finds the div and call clean_up_brand_name on it.
        """
        for category, div_location in lst.items():
            print(f"\n{category}:")
            div_location = self.soup.select_one(div_location)
            self.clean_up_brand_name(div_location)


COCA_WIKI = CocaColaWikiScraper()
COCA_WIKI.iterate_over_list(COCA_WIKI.get_all_div_location())
