import requests
from bs4 import BeautifulSoup


class Nestle_Wiki_Scraper:
    def __init__(self):
        self.url = "https://en.wikipedia.org/wiki/List_of_Nestl%C3%A9_brands"
        self.request = requests.get(self.url)
        self.soup = BeautifulSoup(self.request.content, "html.parser")

    def get_rid_of(self, bs_object):
        for element in bs_object.findAll("li"):
            text = element.get_text()

            if "[" in text and "(" in text:
                text = text.split("(")
                text = text[0].split("[")
                text = text[0].strip()
            elif " –" in text:
                text = text.split(" –")
            elif "[" in text:
                text = text.split("[")
            elif "(" in text:
                text = text.split("(")


            if type(text) is list:
                print(text[0].strip())
            else:
                print(text.strip())

    def get_it(self):
        list = {
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
        for category, div_add in list.items():
            print(f"\nCategory: {category}")
            self.get_rid_of(self.soup.select_one(div_add))

ns = Nestle_Wiki_Scraper()
ns.get_it()
