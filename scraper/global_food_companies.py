"""This module gathers information about companies of gernal mills."""
import re

import requests
from bs4 import BeautifulSoup


class FoodCompaniesFromAllOverTheWordWikiScraper:
    """Returns all food companies from all over the world"""

    def __init__(self):
        self.url = "https://en.wikipedia.org/wiki/List_of_food_companies"
        self.request = requests.get(self.url)
        self.soup = BeautifulSoup(self.request.content, "html.parser")

    @classmethod
    def get_all_div_location(cls):
        """
        Returns a dictionary with locations of the company list, located by css selctor, combind
        with the country of the origin.
        """
        div_locations_list = {
            "Germany": "#mw-content-text > div > ul:nth-child(41)",
            "Austria": "#mw-content-text > div > ul:nth-child(12)",
            "Belgium": "#mw-content-text > div > ul:nth-child(16)",
            "Denmark": "#mw-content-text > div > ul:nth-child(35)",
            "France": "#mw-content-text > div > div:nth-child(39)",
            "Greece": "#mw-content-text > div > ul:nth-child(43)",
            "Italy": "#mw-content-text > div > div:nth-child(51)",
            "Netherlands": "#mw-content-text > div > ul:nth-child(65)",
            "Poland": "#mw-content-text > div > ul:nth-child(77)",
            "Portugal": "#mw-content-text > div > ul:nth-child(79)",
            "Spain": "#mw-content-text > div > ul:nth-child(91)",
            "Switzerland": "#mw-content-text > div > ul:nth-child(97)",
            "United Kingdom": "#mw-content-text > div > div:nth-child(109)",
            "Africa": "#mw-content-text > div > ul:nth-child(6)",
            "Argentina": "#mw-content-text > div > ul:nth-child(8)",
            "Australia": "#mw-content-text > div > div:nth-child(10)",
            "Azerbaijan": "#mw-content-text > div > ul:nth-child(14)",
            "Brazil": "#mw-content-text > div > ul:nth-child(18)",
            "Bulgaria": "#mw-content-text > div > ul:nth-child(20)",
            "Canada": "#mw-content-text > div > div:nth-child(22)",
            "Caribbean": "#mw-content-text > div > ul:nth-child(24)",
            "Chile": "#mw-content-text > div > ul:nth-child(26)",
            "China": "#mw-content-text > div > ul:nth-child(29)",
            "Colombia": "#mw-content-text > div > ul:nth-child(31)",
            "Croatia": "#mw-content-text > div > ul:nth-child(33)",
            "Finland": "#mw-content-text > div > ul:nth-child(37)",
            "Finland": "#mw-content-text > div > ul:nth-child(45)",
            "India": "#mw-content-text > div > div:nth-child(47)",
            "Indonesia": "#mw-content-text > div > ul:nth-child(49)",
            "Ireland": "#mw-content-text > div > div:nth-child(53)",
            "Israel": "#mw-content-text > div > ul:nth-child(55)",
            "Japan": "#mw-content-text > div > ul:nth-child(57)",
            "Kuwait": "#mw-content-text > div > ul:nth-child(59)",
            "Malaysia": "#mw-content-text > div > ul:nth-child(61)",
            "Mexico": "#mw-content-text > div > ul:nth-child(63)",
            "New Zealand": "#mw-content-text > div > div:nth-child(67)",
            "Norway": "#mw-content-text > div > ul:nth-child(69)",
            "Pakistan": "#mw-content-text > div > ul:nth-child(71)",
            "Peru": "#mw-content-text > div > ul:nth-child(73)",
            "Philippines": "#mw-content-text > div > ul:nth-child(75)",
            "Russia": "#mw-content-text > div > ul:nth-child(81)",
            "Saudi Arabia": "#mw-content-text > div > ul:nth-child(83)",
            "Serbia": "#mw-content-text > div > ul:nth-child(85)",
            "Singapore": "#mw-content-text > div > ul:nth-child(87)",
            "South Korea": "#mw-content-text > div > ul:nth-child(89)",
            "Sri Lanka": "#mw-content-text > div > ul:nth-child(93)",
            "Sweden": "#mw-content-text > div > ul:nth-child(95)",
            "Taiwan": "#mw-content-text > div > ul:nth-child(99)",
            "Thailand": "#mw-content-text > div > ul:nth-child(101)",
            "Trinidad and Tobago": "#mw-content-text > div > ul:nth-child(103)",
            "Turkey": "#mw-content-text > div > ul:nth-child(105)",
            "Ukraine": "#mw-content-text > div > ul:nth-child(107)",
            "United States": "#mw-content-text > div > div:nth-child(113)",
            "United States": "#mw-content-text > div > div:nth-child(115)",
            "United States": "#mw-content-text > div > div:nth-child(117)",
            "United States": "#mw-content-text > div > div:nth-child(119)",
            "United States": "#mw-content-text > div > div:nth-child(121)",
            "United States": "#mw-content-text > div > div:nth-child(123)",
            "United States": "#mw-content-text > div > div:nth-child(125)",
            "United States": "#mw-content-text > div > div:nth-child(127)",
            "United States": "#mw-content-text > div > div:nth-child(129)",
            "United States": "#mw-content-text > div > div:nth-child(131)",
            "United States": "#mw-content-text > div > ul:nth-child(133)",
            "United States": "#mw-content-text > div > div:nth-child(135)",
            "United States": "#mw-content-text > div > div:nth-child(137)",
            "United States": "#mw-content-text > div > ul:nth-child(139)",
            "United States": "#mw-content-text > div > div:nth-child(141)",
            "Venezuela": "#mw-content-text > div > ul:nth-child(143)",
            "Vietnam": "#mw-content-text > div > ul:nth-child(145)",
        }
        return div_locations_list

    def iterate_over_list(self, lst):
        """
        Iterates over the list of div locations. Finds the div and call clean_up_company_name on it.
        """
        for country, div_location in lst.items():
            print(f"\n{country}:")
            div_location = self.soup.select_one(div_location)
            self.clean_up_company_name(country, div_location)

    @classmethod
    def save_company(cls, country, company):
        """
        Takes a company name, the origian country
        and saves it with the corporation into the database
        """
        data = {
            "name": company,
            "origin": country,
        }
        requests.post(
            "http://localhost:8000/goodbuyDatabase/save_company/", json=data,
        )

    def clean_up_company_name(self, country, bs_object):
        """
        Takes a BeautifulSoup object, searches for all links in it, interate through it. searches
        for special characters to remove unneeded text from the link text. In the end the name
        gets handed over to the save_company function.
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
                        self.save_company(
                            country, link_text.split(special_char[0])[0].strip()
                        )
                    except IndexError:
                        print(link_text)
                        self.save_company(country, link_text.strip())
        except AttributeError:
            print(" div changed position", str(AttributeError))


GENERAL_MILLS_WIKI = FoodCompaniesFromAllOverTheWordWikiScraper()
GENERAL_MILLS_WIKI.iterate_over_list(GENERAL_MILLS_WIKI.get_all_div_location())
