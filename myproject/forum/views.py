from django.shortcuts import render
from django.http import HttpResponse
def Home(request):
    return render(request,'forum/home.html',context)

def About(request):
    return HttpResponse("<h1>Hello from about</h1>")

def signin (request):
    return HttpResponse("<h1>Hello from sign in and hello from GIT</h1>")

# Create your views here.
