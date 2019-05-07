# ratelyyGitHub
It’s about building a tool to raise awareness what impact your consumptions have on the plane, the society and nature and also empowers people to consume based on their own ethical and moral consumer profile.

### Project: ratelyy
### Authors: Darjusch Schrand & Anthony Sherrill
### 15. April 2019
# Technical Paper - Goodbuy
The Goodbuy project gathers data about concerns, companies and products to analyse them. To do so, there is a MySQL database in place, which is accessible through a web application base on the Django web framework.
## General
Main backend programming language is Python3. The web framework is Django version 2. structure all applications (modules) in Django modular, which also means we work with name spaces all the time. The software architecture is MVC.
## Get the project
First, go to Github https://github.com/5h3rr1ll/ratelyyGitHub and clone the project.
## Required software and packages
Note: Make sure you have pip3 and homebrew (homebrew on Mac, if you use windows use an equivalent)
## Packages: Django 2.1.7 , Python 3.7.3 , mysqlclient 1.4.2. , Pillow 5.4.1 , requests 2.21.0 , django-ssl
Run the server
Go in the terminal to the ratelyyDjango folder inside ratelyyGitHub-Master.
## Run the server with the command: $ python3 manage.py runserver
Go in your web browser to address http://127.0.0.1:8000 and you will automatically become redirected to the login site, where you can log in with user TestUser and password Nix123456. To you access the admin panel visit http://127.0.0.1:8000/admin or click the link in the menu.
## Troubleshooting
If you encounter problems with installing mysqlclient this resource might help: https://stackoverflow.com/questions/43740481/python-setup-py-egg-info-mysqlclient
Also, make sure you always use the correct python version while executing the terminal commands. Another problem could be “max_user_connections” open django python shell, enter “from django import db” and execute “db.connections.close_all()”. 
## Project Files
Inside ratelyyDatabase you will find the admin.py in which you can configure what is displayed on the Admin page.
## Modules / Django Apps
### ratelyyDatabase
Inside the ratelyyDatabase directory, you will find the models.py file is for the database here you can configure your tables, define the input type and the relations between the tables. If you have done the changes, you have to migrate it to also make the changes in the database.
### ratelyyDjango
Inside ratelyyDjango you will find the middleware.py which is a file for security in Django, for example, we defined here that you can only access specific sites when you are logged in. There you also find the settings.py where you need to announce new applications and where you also set e.g. the database settings and much more.
### mvpScanWebApp
In this app main functions is to add products to the database. To lower the error while entering the product code, we are using web SDK from Scandit, to scan the code. At the moment everything happens in templates/mypScanWebApp/gtin.html . There the SDK gets loaded and via js. the scanned code gets sent to the server where the urls.py gets triggered to either add a product or to show that the product already exists. The business logic for that you will find in the views.py, as always.
### mvpLogograb
The main logic for the foundation of the feedback-to-a-product-function happens in mvpLogoGrab: Two functions Upload picture OR take pictures. To upload the picture and then determine the logo we use an API (LogoGrab) which can be found in the script.js (logoGrabWebScanner()) placed in the folder mvpLogoGrab/static/script.js .
The logo name is then sent through a post request to the server also in the script.js (requestLogonameData()).
The data is then queried on the server side you can find it in the views.py file(get_data() & post()).
#Explain more in detail
To configure the videoStream / Picture taking take a look into the script.js
### Accounts
In accounts happens everything around users. You find in the template folder the templates for registration, login, profile, change password, edit profile, password reset, log out and so on. In accounts is a forms.py which defines how the registrations pages look like and the edit profile pages.
### Home
The most import file in home app is the base.html. The base.html is like the index.html file of the page. Every other template html file inherits for that file by using {% extends “base.html” %} . Beside of that you can post posts at the home.html side and add other users of the page as friend.
