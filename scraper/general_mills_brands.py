"""This module gathers information about brands and companies of corperations."""
import os
import re

import requests
from bs4 import BeautifulSoup


class GeneralMillsWikiScraper:
    """Returns brands of General Mills"""

    def __init__(self):
        self.url = "https://en.wikipedia.org/wiki/General_Mills"
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
            f"{os.environ.get('CURRENT_HOST')}/goodbuyDatabase/save_brand/", json=data,
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
                    except IndexError:
                        print(str(IndexError), link_text)
                        self.save_brand(link_text.strip())
        except AttributeError:
            print(" div changed position", str(AttributeError))

    @classmethod
    def get_all_div_location(cls):
        """
        Returns a dictionary with locations of the brand list, located by css selctor, combind with
        with the sections title.
        """
        div_locations_list = {
            "Breakfast cereals": "#mw-content-text > div > div:nth-child(55)",
            "Baking goods": "#mw-content-text > div > div:nth-child(62)",
            "Grain snacks": "#mw-content-text > div > div:nth-child(66)",
            "Meal products": "#mw-content-text > div > div:nth-child(69)",
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


GENERAL_MILLS_WIKI = GeneralMillsWikiScraper()
GENERAL_MILLS_WIKI.iterate_over_list(GENERAL_MILLS_WIKI.get_all_div_location())
