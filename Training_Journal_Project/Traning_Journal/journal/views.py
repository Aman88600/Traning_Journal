from django.shortcuts import render
from django.http import HttpResponse
from .models import student
# Create your views here.
def index(request):
    return render(request, "journal/index.html")

def login(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        user_password = request.POST.get("user_password")
        f = student.objects.all()
        f = list(f)
        user_exists = 0
        for i in f:
            if (str(user_name) == str(i.name)) and (str(user_password) == str(i.password)):
                user_exists = 1
        if user_exists == 1:
            m = "User Exists"
            return render(request, "journal/login.html", {"message" : m})
        else:
            m = "User Doesn't Exist"
            return render(request, "journal/login.html", {"message" : m})
    return render(request, "journal/login.html")

def signup(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        user_password = request.POST.get("user_password")
        f = student(name = user_name, password = user_password)
        f.save()
        return render(request, "journal/login.html")
    return render(request, "journal/signup.html")
