# from django.test import TestCase
# from scraper.kelloggs_brands import KelloggsWikiScraper
#
# class BrandScraper(TestCase):
#
#     def setUp(self):
#         self.kelloggs = KelloggsWikiScraper()
#
#
#     def test_if_scraped_website_structure_changed(self):
#         div_locations_list = self.kelloggs.get_all_div_location()
#         try:
#             for category, div_location in div_locations_list.items():
#                 div_location = self.kelloggs.soup.select_one(div_location)
#                 if div_location.findAll("li") == []:
#                     print('empty Error')
#                 break
#         except AttributeError as e:
#             print(str(e), ' div changed position ')
