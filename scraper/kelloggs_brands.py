import requests
from bs4 import BeautifulSoup

import re


class KelloggsWikiScraper:
    def __init__(self):
        self.url = "https://en.wikipedia.org/wiki/Kellogg%27s"
        self.request = requests.get(self.url)
        self.soup = BeautifulSoup(self.request.content, "html.parser")

    def save_brand(self, brand):
        data = {
            "name": brand,
            "corporation": "Kellogg's",
        }
        requests.post(
            "http://localhost:8000/goodbuyDatabase/save_brand/", json=data,
        )

    def clean_up_brand_name(self, bs_object):
        try:
            if bs_object.findAll("li") == []:
                print('empty Error')
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
            print(str(e), ' div changed position ')


    def get_all_div_location(self):
        div_locations_list = {
            "Products" : "#mw-content-text > div > div:nth-child(26)",
            "Cereal" : "#mw-content-text > div > div:nth-child(30)",
        }
        return div_locations_list

    def iterate_over_list(self, lst):
        for Category, div_location in lst.items():
            print(f"\nBrands starting with: {Category}")
            div_location = self.soup.select_one(div_location)
            self.clean_up_brand_name(div_location)



# kelloggs_wiki = KelloggsWikiScraper()
# div_locations_list = kelloggs_wiki.get_all_div_location()
# kelloggs_wiki.iterate_over_list(div_locations_list)
