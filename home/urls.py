from django.urls import path

from . import views


app_name = "home"

urlpatterns = [
    path("", views.start_screen, name="start_screen"),
    path("posts/", views.PostView.as_view(), name="posts"),
    path("posts_dev/", views.home, name="posts"),
    path("connect/<operation>/<pk>/", views.change_friends, name="change_friends"),
    path("rating/<code>", views.rating, name="rating"),
]
