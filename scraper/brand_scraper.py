"""This module gathers information about brands and companies of corporations."""

import json
import os
import re
import sys

import requests
from bs4 import BeautifulSoup


class BColors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class BrandScraper:
    """This class loads a JSON of the top 10 food corporations,
    iterate over it and save their brands to the Goodbuy-Database"""

    def __init__(self):
        with open(os.path.join(sys.path[0], "corps.json"), "r") as f:
            self.corps_dict = json.load(f)

    def get_all(self):
        for corp in self.corps_dict.keys():
            print(f"\n{BColors.HEADER}{corp}{BColors.ENDC}")
            url = self.corps_dict[corp]["url"]
            request = requests.get(url)
            soup = BeautifulSoup(request.content, "html.parser")
            self.iterate_over_json(self.corps_dict[corp]["divs"], soup, corp)
            try:
                print(f"\n{BColors.OKBLUE}Brand List{BColors.ENDC}")
                for brand in self.corps_dict[corp]["brand_list"]:
                    print(brand)
                    self.save_brand(brand, corp)
            except Exception as e:
                print(
                    f"{BColors.FAIL}brand list is empty{BColors.ENDC}", str(e)
                )

    def get_single_corp(self, corp_name):
        print(f"\n{BColors.HEADER}{corp_name}{BColors.ENDC}")
        url = self.corps_dict[corp_name]["url"]
        request = requests.get(url)
        soup = BeautifulSoup(request.content, "html.parser")
        self.iterate_over_json(
            self.corps_dict[corp_name]["divs"], soup, corp_name
        )
        try:
            print(f"\n{BColors.OKBLUE}Brand List{BColors.ENDC}")
            for brand in self.corps_dict[corp_name]["brand_list"]:
                print(brand)
                self.save_brand(brand, corp_name)
        except Exception as e:
            print(f"{BColors.FAIL}brand list is empty{BColors.ENDC}", str(e))

    @classmethod
    def save_brand(cls, brand, corp):
        """
        Takes a brand name and saves it with the corporation into the database
        """
        data = {
            "name": brand,
            "corporation": corp,
        }
        requests.post(
            f"{os.environ.get('CURRENT_HOST')}/goodbuyDatabase/save_brand/",
            json=data,
        )

    def clean_up_brand_name(self, bs_object, corp):
        """
        Takes a BeautifulSoup object, searches for all links in it, iterate
        through it. searches for special characters to remove unneeded text
        from the link text. In the end the name gets handed over to the
        save_brand function.
        """
        try:
            if bs_object.findAll("li"):
                for list_element in bs_object.findAll("li"):
                    link_text = list_element.get_text()
                    special_char = re.findall(
                        r"[\][–)(,}:]|[0-9]{4}", link_text
                    )
                    try:
                        print(link_text.split(special_char[0])[0])
                        self.save_brand(
                            link_text.split(special_char[0])[0].strip(), corp
                        )
                    except IndexError:
                        print(link_text)
                        self.save_brand(link_text.strip(), corp)
            elif bs_object.findAll("td"):
                for list_element in bs_object.findAll("a"):
                    link_text = list_element.get_text()
                    special_char = re.findall(
                        r"[\][–)(,}:]|[0-9]{4}", link_text
                    )
                    try:
                        print(link_text.split(special_char[0])[0])
                        self.save_brand(
                            link_text.split(special_char[0])[0].strip(), corp
                        )
                    except IndexError:
                        print(link_text)
                        self.save_brand(link_text.strip(), corp)
            else:
                print(f"{BColors.FAIL}empty Error{BColors.ENDC}")
        except AttributeError:
            print(
                f"{BColors.FAIL}div changed position{BColors.ENDC}",
                str(AttributeError),
            )

    def iterate_over_json(self, lst, soup, corp):
        """
        Iterates over the json object. Finds the list of div and call
        clean_up_brand_name on it.
        """
        for category, div_location in lst.items():
            print(f"{BColors.OKGREEN}\n{category}{BColors.ENDC}")
            div_location = soup.select_one(div_location)
            self.clean_up_brand_name(div_location, corp)


if __name__ == "__main__":
    action_handler = BrandScraper()
    action_handler.get_all()
