from django.shortcuts import render
from django.http import HttpResponse
from .models import student
# Create your views here.
def index(request):
    return render(request, "journal/index.html")

def login(request):
    return render(request, "journal/login.html")

def signup(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        user_password = request.POST.get("user_password")
        f = student(name = user_name, passowrd = user_password)
        f.save()
        return render(request, "journal/login.html")
    return render(request, "journal/signup.html")
