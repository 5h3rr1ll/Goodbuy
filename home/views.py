from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from goodbuyDatabase.models import Product, Corporation, Rating
from .models import Post, Friend
from .forms import HomeForm


@login_required
def rating(request, code):
    product = Product.objects.get(code=code)
    corporation = Corporation.objects.get(name=product.corporation)
    rating = Rating.objects.get(corporation=corporation.id)
    if rating.animals == None or rating.humans == None  or rating.environment == None:
        total_rating = 0
    else:
        total_rating = round((rating.animals+rating.humans+rating.environment)/3)*10
    args = {
        "product":product,
        "rating_result":total_rating,
        "rating":rating,
        "corporation":corporation,
    }
    return render(request, "home/rating.html",args)

@login_required
def start_screen(request):
    return render(request,"home/start.html")

@login_required
def posts(request):
    context = {
        "posts": Post.objects.all(),
    }
    return render(request, "home/posts.html", context)

class PostListView(ListView):
    model = Post
    template_name = "home/posts.html"
    context_object_name = "posts"
    # the minus infront of date_posted bringst the newst post to the top
    ordering = ["-date_posted"]
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = "home/user_posts.html"
    context_object_name = "posts"
    # the minus infront of date_posted bringst the newst post to the top
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title","content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title","content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostView(TemplateView):
    template_name = "home/posts.html"

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by("-created")
        users = User.objects.exclude(id=request.user.id)
        # TODO: next query needs to make sure to retrun an object in case user
        # has no friends, otherwise site crashes
        friend = Friend.objects.get_or_create(current_user=request.user)
        try:
            friends = friend.users.all()
            args = {"form":form,"posts":posts,"users":users,"friends":friends}
        except:
            friends = ()
            args = {"form":form,"posts":posts,"users":users,"friends":friends}
            return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            # is a safty method to make sure that no bad code is in the forms
            # like a SQL injection
            text = form.cleaned_data["post"]
            form = HomeForm()
            return redirect("home:posts")

        args = {"form":form, "text":text}
        return render(request, self.template_name, args)

@login_required
def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == "add":
        Friend.make_friend(request.user, friend)
    elif operation == "remove":
        Friend.lose_friend(request.user, friend)
    return redirect("home:posts")

@login_required
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
