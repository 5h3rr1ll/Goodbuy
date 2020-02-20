from brand_scraper import BrandScraper
from sys import argv, exit


if __name__ == "__main__":
    brand_scraper = BrandScraper()
    try:
        brand_scraper.get_single_corp(argv[1])
    except Exception:
        n = 1

        while True:
            print("Choose the number of the Concern whose brands you would like to get.")
            n = 1
            for corp in brand_scraper.corps_dict.keys():
                print(f"{n}. {corp}")
                n += 1
            input = int(input())
            if input in range(1, 11):
                brand_scraper.get_single_corp(list(brand_scraper.corps_dict.keys())[input-1])
                exit(0)
            else:
                print("Please choose a number between 1 and 10")
                exit(1)
