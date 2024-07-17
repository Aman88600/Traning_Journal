from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "journal/index.html")

def login(request):
    return render(request, "journal/login.html")

def signup(request):
    return render(request, "journal/signup.html")
