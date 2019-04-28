#Most interisting views are logo_grab and get_data
#logo_grab() does the following
#Postrequest with a picture that was made on our website to the logoGrabApi
#and requesting datafrom the Database with the response
#get_data() does:
#Recieving the logoname of an uploaded picture and requesting the database to give associated data

import requests
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from mvpLogoGrab.forms import (
    RegistrationForm,
    EditProfileForm,
)
from ratelyyDatabase.models import (
    Product,
    Concern,
)
# Create your views here.
def home(request):
    args = {'Home' : 'Home'}
    return render(request, 'mvpLogoGrab/home.html', args)

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/mvpLogoGrab/profile")
        else:
            form = RegistrationForm()
            args = {"form": form}
            return render(request, "mvpLogoGrab/reg_failed.html", args)
    else:
        form = RegistrationForm()
        args = {"form": form}
        return render(request, "mvpLogoGrab/reg_form.html", args)

def profile(request):
    args = {'user': request.user}
    return render(request, 'mvpLogoGrab/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/mvpLogoGrab/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {"form": form}
        return render(request, 'mvpLogoGrab/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/mvpLogoGrab/profile')
        else:
            return redirect('/mvpLogoGrab/change-password')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {"form": form}
        return render(request, 'mvpLogoGrab/change_password.html', args)

#Postrequest with a picture that was made on our website to the logoGrabApi
#and requesting datafrom the Database with the response
def logo_grab(request):
    url = "https://api.logograb.com/detect"
    querystring = {
        #Image of barilla has to be changed to pic
        "mediaUrl" : "https://tinyurl.com/y6jxnaov",
        "developerKey" : "nb9n3ra9fpmrk0u0binh2b03jr3acq510tqhldmr"
        }
    #Accessing the logoname of the product inside the JSON
    response = requests.request("POST", url, params=querystring)
    print("function logo_grab")
    print(response)
    json_response = response.json()
    print(json_response["data"]["detections"][0]["name"])
    product_name = json_response["data"]["detections"][0]["name"]
    product_name = product_name.replace("-", " ")
    #Requesting data from the database with the logoname
    product_data = Product.objects.get(name=product_name)
    concern_data = Concern.objects.get(name=product_data.concern)
    #Updating Statcounter
    print(product_data.stat_counter)
    product_data.stat_counter += 1
    product_data.save()
    #Saving the data into a dict to display it on the html page
    args = {
        "id" : product_data.id,
        "name" : product_data.name,
        "logo" : product_data.logo,
        "wiki" : product_data.wiki,
        "code" : product_data.code,
        "group" : product_data.name,
        "brand" : product_data.brand,
        "concern" : product_data.concern,
        "main_category" : product_data.main_category,
        "sub_category" : product_data.sub_category,
        "image" : product_data.image,
        "created" : product_data.created,
        "updated" : product_data.updated,
        "rating" : concern_data.rating,
        "concern_origin" : concern_data.origin,

    }
    #to get a result change to return render(request, 'mvpLogoGrab/data.html', args)

    return render(request, 'mvpLogoGrab/logo_grab.html', args)

#Recieving the logoname of an uploaded picture and requesting the database to give associated data
def get_data(request):
    print("function get_data")
    product_name = request.GET.get("name", "Not found")
    product_data = Product.objects.get(name=product_name)
    concern_data = Concern.objects.get(name=product_data.concern)

    #Saving the data into a dict to display it on the html page
    args = {
        "id" : product_data.id,
        "name" : product_data.name,
        "logo" : product_data.logo,
        "wiki" : product_data.wiki,
        "code" : product_data.code,
        "group" : product_data.name,
        "brand" : product_data.brand,
        "concern" : product_data.concern,
        "main_category" : product_data.main_category,
        "sub_category" : product_data.sub_category,
        "image" : product_data.image,
        "created" : product_data.created,
        "updated" : product_data.updated,
        "rating" : concern_data.rating,
        "concern_origin" : concern_data.origin,

    }
    return render(request, 'mvpLogoGrab/data.html', args)
#Testing post request for client to server data will be deleted later.
def post(request):
    print("function post")
    print(request)
    body = request.body
    payload = {"image" : body}
    url = "https://api.imgur.com/3/upload"
    client_id = "121963ba11eb969"


    p = requests.post(url, payload, client_id)

    print(p)

    args = {
        "Post" : "Post"
    }
    return render(request, 'mvpLogoGrab/post.html', args)

def dataUrl(request, dataUrl):
    print("we print here" + len(dataUrl))
    args = {
        "test" : "test"
    }
    return render(request, 'mvpLogoGrab/post.html', args)