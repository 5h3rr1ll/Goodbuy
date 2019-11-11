from django.test import TestCase
from goodbuyDatabase.models import Country, Store, Corporation, Rating, Company, Brand

class TestModels(TestCase):

    def setUp(self):
        self.country_obj = Country.objects.create(
            name='Frankreich',
            code='FR'
        )

        self.store_obj = Store.objects.create( 
            name='Edeka',
            country=Country.objects.get(name='Frankreich')
        )

        self.corporation_obj = Corporation.objects.create(
            name='Apple',
            logo='www.apple/jpg.de',
            wiki='www.apple/wiki.de',
            origin=Country.objects.get(name='Frankreich')
        )

        self.rating_obj = Rating.objects.create(
            humans = 8,
            humans_description = 'They treat their workers good',
            environment = 2,
            environment_description = 'The environment has to suffer a lot because of their produced waste',
            animals = 5,
            animals_description = 'They don\'t have a lot to do with anmials',
            corporation = Corporation.objects.get(name='Apple')
        )

        self.company_obj = Company.objects.create(
            name = 'Amazon',
            logo = 'www.Amazon/logo.de',
            wiki = 'www.wiki/Amazon.de',
            corporation = Corporation.objects.get(name='Apple'),
            origin = Country.objects.get(code='FR')
        )

        self.brand_obj = Brand.objects.create(
            name = 'Factory',
            company = Company.objects.get(name='Amazon'),
            corporation = Corporation.objects.get(name='Apple')
        )

        
    def test_if_country_creation_works(self):
        country = Country.objects.get(name='Frankreich')
        self.assertEqual(country.code, 'FR')

    def test_if_store_creation_works(self):
        store = Store.objects.get(name='Edeka')
        self.assertEqual(store.name, 'Edeka')

    def test_if_corporation_creation_works(self):
        corportaion = Corporation.objects.get(name='Apple')
        self.assertEqual(corportaion.wiki, 'www.apple/wiki.de')

    def test_if_rating_creation_works(self):
        rating = Rating.objects.get(humans=8)
        self.assertEqual(rating.animals, 5)
    
    def test_if_company_creation_works(self):
        company = Company.objects.get(logo='www.Amazon/logo.de')
        self.assertEqual(company.name, 'Amazon')

    def test_if_brand_creation_works(self):
        brand = Brand.objects.get(name='Factory')
        self.assertEqual(brand.name, 'Factory')

    