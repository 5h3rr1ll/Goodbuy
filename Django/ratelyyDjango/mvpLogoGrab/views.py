from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    numbers = [25,5,6,8]
    name = "Darjusch Schrand"
    args = { 'myName' : name, 'numbers' : numbers}
    return render(request, 'mvpLogoGrab/login.html', args)
