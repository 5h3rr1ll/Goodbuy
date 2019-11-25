from django.urls import path
from scraper.views import scrape

app_name = "scraper"

urlpatterns = [
    path("<str:code>/", scrape, name="scrape"),
]
