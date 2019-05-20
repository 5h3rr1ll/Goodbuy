from django.urls import path

from . import views as home_view


app_name = "home"

urlpatterns = [
    path("", home_view.start_screen, name="home"),
    path("posts/", home_view.PostListView.as_view(), name="post_list"),
    path("post/new/", home_view.PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/update/", home_view.PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", home_view.PostDeleteView.as_view(), name="post_delete"),
    path("post/<int:pk>/", home_view.PostDetailView.as_view(), name="post_detail"),
    path("posts/<str:username>/", home_view.UserPostListView.as_view(), name="user_posts"),
    path("rating/<code>", home_view.rating, name="rating"),
    path("about/", home_view.about, name="blog_about"),
    path("connect/<operation>/<int:pk>/", home_view.change_friends, name="change_friends"),
]
