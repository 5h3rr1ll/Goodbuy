from django.urls import path

from . import views as home_view


app_name = "home"

urlpatterns = [
    path("", home_view.start_screen, name="home"),
    path("posts/", home_view.PostListView.as_view(), name="posts"),
    path("post/<int:pk>/", home_view.PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", home_view.PostUpdateView.as_view(), name="post-update"),
    path("post/new/", home_view.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/delete/", home_view.PostDeleteView.as_view(), name="post-delete"),
    path("connect/<operation>/<int:pk>/", home_view.change_friends, name="change_friends"),
    path("rating/<code>", home_view.rating, name="rating"),
    path("about/", home_view.about, name="blog-about"),
    path("user/<str:username>/", home_view.UserPostListView.as_view(), name="user-posts"),
]
