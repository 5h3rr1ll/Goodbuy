from django.urls import path
from brandScraper import views

app_name = "brandScraper"

urlpatterns = [
    path('', views.scrape, name='scrape'),
]
