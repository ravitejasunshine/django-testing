from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Welcome to Django world")
def Home(request):
    return HttpResponse("<h1>Welcome to Home page</h1>") 
def GoodBye(request):
    return HttpResponse("<h1 style='color:red;font-family:tohama;font-size:40px;text-decoration:underline'>Thanks for visiting soon</h1>") 
          