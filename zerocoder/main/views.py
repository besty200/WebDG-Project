from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'main/index.html')

def new(request):
    return render(request,'main/new.html')

def about(request):
    return render(request,'main/about.html')

def contact(request):
    return render(request,'main/contact.html')

def services(request):
    return render(request,'main/services.html')

def first(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def test(request):
    return HttpResponse("<h1>Это тестовая страница</h1>")

def data(request):
    return HttpResponse("<h1>Это страница основного сайта с данными</h1>")
