from django.test import TestCase

from goodbuyDatabase.models import (
    Brand,
    Company,
    Corporation,
    Country,
    Product,
    Rating,
    Store,
)


class TestModels(TestCase):
    def setUp(self):
        self.country_obj = Country.objects.create(name="Frankreich", code="FR")

        self.store_obj = Store.objects.create(
            name="Edeka", country=Country.objects.get(name="Frankreich")
        )

        self.corporation_obj = Corporation.objects.create(
            name="Apple",
            logo="www.apple/jpg.de",
            wiki="www.apple/wiki.de",
            origin=Country.objects.get(name="Frankreich"),
        )

        self.rating_obj = Rating.objects.create(
            women_value=8,
            women_rating_text="They treat their female workers good",
            land_value=2,
            land_rating_text="""
            The environment has to suffer a lot because of their produced waste
            """,
            climate_value=5,
            climate_rating_text="They don't have a lot to do with climate",
            corporation=Corporation.objects.get(name="Apple"),
        )

        self.company_obj = Company.objects.create(
            name="Amazon",
            logo="www.Amazon/logo.de",
            wiki="www.wiki/Amazon.de",
            corporation=Corporation.objects.get(name="Apple"),
            origin=Country.objects.get(code="FR"),
        )

        self.brand_obj = Brand.objects.create(
            name="Factory",
            company=Company.objects.get(name="Amazon"),
            corporation=Corporation.objects.get(name="Apple"),
        )

    def create_country(self, name="Germany"):
        return Country.objects.create(name=name)

    def create_product(self, name="Snickers", code="123456"):
        return Product.objects.create(name=name, code=code)

    def test_if_country_creation_works(self):
        country = Country.objects.get(name="Frankreich")
        self.assertEqual(country.code, "FR")

    def test_if_store_creation_works(self):
        store = Store.objects.get(name="Edeka")
        self.assertEqual(store.name, "Edeka")

    def test_if_corporation_creation_works(self):
        corportaion = Corporation.objects.get(name="Apple")
        self.assertEqual(corportaion.wiki, "www.apple/wiki.de")

    def test_if_rating_creation_works(self):
        rating = Rating.objects.get(women_value=8)
        self.assertEqual(rating.climate_value, 5)

    def test_if_company_creation_works(self):
        company = Company.objects.get(logo="www.Amazon/logo.de")
        self.assertEqual(company.name, "Amazon")

    def test_if_brand_creation_works(self):
        brand = Brand.objects.get(name="Factory")
        self.assertEqual(brand.name, "Factory")

    def test_create_country(self):
        country = self.create_country()
        self.assertTrue(isinstance(country, Country))
        self.assertEqual(country.__str__(), country.name)

    def test_create_product(self):
        product = self.create_product()
        self.assertTrue(isinstance(product, Product))
        self.assertEqual(product.__str__(), product.name)
