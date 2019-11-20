from django.urls import path
from scraper import cc_lookup

app_name = "scraper"

urlpatterns = [
    path("<str:code>/", cc_lookup.cc_lookup, name="cc_lookup"),
]
