# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import HomeForm
from .models import Post, Friend
from goodbuyDatabase.models import Product, Corporation, Rating


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

def start_screen(request):
    return render(request,"home/start.html")

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

def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == "add":
        Friend.make_friend(request.user, friend)
    elif operation == "remove":
        Friend.lose_friend(request.user, friend)
    return redirect("home:posts")
