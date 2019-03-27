from django.conf.urls import url
from home.views import HomeView

app_name = "home"

urlpatterns = [
    url(r"^$", HomeView.as_view(), name="home")
]
