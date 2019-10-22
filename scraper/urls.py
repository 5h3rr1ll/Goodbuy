from django.urls import path
from scraper import views

app_name = "scraper"

urlpatterns = [
    path('<str:code>/', views.scrape, name='scrap'),
]
