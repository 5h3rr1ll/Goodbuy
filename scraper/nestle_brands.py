import requests
from bs4 import BeautifulSoup


class Nestle_Wiki_Scraper:
    def __init__(self):
        self.url = "https://en.wikipedia.org/wiki/List_of_Nestl%C3%A9_brands"
        self.request = requests.get(self.url)
        self.soup = BeautifulSoup(self.request.content, "html.parser")

    def save_brand(self, brand):
        data = {
            "name" : brand,
            "corporation" : "Nestlé",
        }
        requests.post("http://localhost:8000/goodbuyDatabase/save_brand/", json=data, )

    def get_rid_of(self, bs_object):
        for list_element in bs_object.findAll("li"):
            link_text = list_element.get_text()

            if "[" in link_text and "(" in link_text:
                link_text = link_text.split("(")
                link_text = link_text[0].split("[")
                link_text = link_text[0].strip()
            elif " –" in link_text:
                link_text = link_text.split(" –")
            elif "[" in link_text:
                link_text = link_text.split("[")
            elif "(" in link_text:
                link_text = link_text.split("(")

            if type(link_text) is list:
                print(link_text[0].strip())
                self.save_brand(link_text[0].strip())
            else:
                print(link_text.strip())
                self.save_brand(link_text.strip())

    def get_all_categories(self):
        list_of_div_locations = {
            "Beverages": "#mw-content-text > div > div:nth-child(6)",
            "Coffee": "#mw-content-text > div > div:nth-child(8)",
            "Water": "#mw-content-text > div > div:nth-child(10)",
            "Cereals": "#mw-content-text > div > div:nth-child(12)",
            "Chilled": "#mw-content-text > div > div:nth-child(15)",
            "Choclate & Co.": "#mw-content-text > div > div:nth-child(17)",
            "Foodservice products": "#mw-content-text > div > ul:nth-child(19)",
            "Frozen food": "#mw-content-text > div > div:nth-child(21)",
            "Frozen Dessert": "#mw-content-text > div > div:nth-child(23)",
            "Healthcare nutrition": "#mw-content-text > div > div:nth-child(25)",
            "Infant foods": "#mw-content-text > div > div:nth-child(27)",
            "Performance nutrition": "#mw-content-text > div > ul:nth-child(29)",
            "Petcare": "#mw-content-text > div > div:nth-child(31)",
            "Purina petcare products": "#mw-content-text > div > div:nth-child(34)",
            "Refrigerated products": "#mw-content-text > div > ul:nth-child(36)",
            "Seasonings": "#mw-content-text > div > ul:nth-child(39)",
            "Shelf stable": "#mw-content-text > div > ul:nth-child(41)",
            "Yogurt": "#mw-content-text > div > div:nth-child(43)",
        }
        for category, div_location in list_of_div_locations.items():
            print(f"\nCategory: {category}")
            self.get_rid_of(self.soup.select_one(div_location))


nestle_wiki = Nestle_Wiki_Scraper()
nestle_wiki.get_all_categories()
