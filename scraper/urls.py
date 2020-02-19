from django.urls import path
from scraper.django_cc_crawler import scrape as local_scrape

app_name = "scraper"

urlpatterns = [
    path("<str:code>/locally", local_scrape, name="local_scrape"),
    # path("<str:code>/", aws_lambda_scrape, name="aws_lambda_scrape"),
]
