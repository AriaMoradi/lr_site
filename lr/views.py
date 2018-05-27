from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.template import Context, loader
from .models import User

def login(request):
    if request.method == 'GET' and 'username' in request.GET:
        u = User.objects.filter(username__exact=request.GET['username'],password__exact=request.GET['password'])
        if u.first() == None:
            return HttpResponse("Username or Password is incorrect!")
        else:
            return HttpResponse("Logged in successfully!")
    else:
        return render(request,"login.html")


def register(request):
    if request.method == 'GET' and 'username' in request.GET:
        u = User.objects.filter(username__exact=request.GET['username'])
        if u.first() == None:
            u = User(username=request.GET['username'],password=request.GET['username'],email=request.GET['email'])
            u.save()
            return HttpResponse("User registered successfully!")
        else:
            return HttpResponse("User exists!")
    else:
        return render(request, "register.html")