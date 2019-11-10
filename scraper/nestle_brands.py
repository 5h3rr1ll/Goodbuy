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
                print(text)
            elif "[" in text:
                text = text.split("[")
            elif "(" in text:
                text = text.split("(")

            if type(text) is list:
                print(text[0].strip())
            else:
                print(text.strip())

    def get_beverages(self):
        print("\nGetting Nestlé's Beverages:")
        self.get_rid_of(
            self.soup.select_one("#mw-content-text > div > div:nth-child(6)")
        )

    def get_coffee(self):
        print("\nGetting Nestlé's Coffee:")
        self.get_rid_of(
            self.soup.select_one("#mw-content-text > div > div:nth-child(8)")
        )

    def get_water(self):
        print("\nGetting Nestlé's Water:")
        self.get_rid_of(
            self.soup.select_one("#mw-content-text > div > div:nth-child(10)")
        )

    def get_cereals(self):
        print("\nGetting Nestlé's Cereals:")
        self.get_rid_of(
            self.soup.select_one("#mw-content-text > div > div:nth-child(12)")
        )

    def get_chilled(self):
        print("\nGetting Nestlé's Chilled:")
        self.get_rid_of(
            self.soup.select_one("#mw-content-text > div > div:nth-child(15)")
        )

    def get_chocolate_confectionery_and_baked_goods(self):
        print("\nGetting Nestlé's Choclate & Co.:")

        self.get_rid_of(
            self.soup.select_one("#mw-content-text > div > div:nth-child(17)")
        )

    def get_foodservice_products(self):
        print("\nGetting Nestlé's Foodservice products:")

        self.get_rid_of(
            self.soup.select_one("#mw-content-text > div > ul:nth-child(19)")
        )

    def get_frozen_food(self):
        print("\nGetting Nestlé's Frozen food:")

        self.get_rid_of(
            self.soup.select_one("#mw-content-text > div > div:nth-child(21)")
        )

    def get_frozen_dessert(self):
        print("\nGetting Nestlé's Frozen Dessert:")

        self.get_rid_of(
            self.soup.select_one("#mw-content-text > div > div:nth-child(23)")
        )

    def get_healthcare_nutrition(self):
        print("\nGetting Nestlé's Healthcare nutrition:")

        self.get_rid_of(
            self.soup.select_one("#mw-content-text > div > div:nth-child(25)")
        )

    def get_infant_foods(self):
        print("\nGetting Nestlé's Infant foods:")

        self.get_rid_of(
            self.soup.select_one("#mw-content-text > div > div:nth-child(25)")
        )

    def get_performance_nutrition(self):
        print("\nGetting Nestlé's Performance nutrition:")

        self.get_rid_of(
            self.soup.select_one("#mw-content-text > div > ul:nth-child(29)")
        )

    def get_petcare(self):
        print("\nGetting Nestlé's Petcare:")

        self.get_rid_of(
            self.soup.select_one("#mw-content-text > div > div:nth-child(31)")
        )

    def get_purina_petcare_products(self):
        print("\nGetting Nestlé's Purina petcare products:")

        self.get_rid_of(
            self.soup.select_one("#mw-content-text > div > div:nth-child(34)")
        )

    def get_refrigerated_products(self):
        print("\nGetting Nestlé's Refrigerated products:")

        self.get_rid_of(
            self.soup.select_one("#mw-content-text > div > ul:nth-child(36)")
        )

    def get_seasonings(self):
        print("\nGetting Nestlé's Seasonings:")

        self.get_rid_of(
            self.soup.select_one("#mw-content-text > div > ul:nth-child(39)")
        )

    def get_shelf_stable(self):
        print("\nGetting Nestlé's Shelf stable:")

        self.get_rid_of(
            self.soup.select_one("#mw-content-text > div > ul:nth-child(41)")
        )

    def get_yogurt(self):
        print("\nGetting Nestlé's Yogurt:")

        self.get_rid_of(
            self.soup.select_one("#mw-content-text > div > div:nth-child(43)")
        )


ns = Nestle_Wiki_Scraper()
ns.get_beverages()
ns.get_coffee()
ns.get_water()
ns.get_cereals()
ns.get_chilled()
ns.get_chocolate_confectionery_and_baked_goods()
ns.get_foodservice_products()
ns.get_frozen_food()
ns.get_frozen_dessert()
ns.get_healthcare_nutrition()
ns.get_infant_foods()
ns.get_performance_nutrition()
ns.get_petcare()
ns.get_purina_petcare_products()
ns.get_refrigerated_products()
ns.get_seasonings()
ns.get_shelf_stable()
ns.get_yogurt()
