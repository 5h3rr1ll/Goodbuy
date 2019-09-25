from django.urls import path
from codeScanner import views

app_name = "codeScanner"

urlpatterns = [
    path('', views.scanCode, name='codeScanner'),
]
