from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, "shop/index.html")


def about(request):
    return render(request, "shop/index.html")


def content(request):
    return HttpResponse("thsi is a content")


def tracker(request):
    return render(request, "shop/index.html")


def search(request):
    return render(request, "shop/index.html")


def productView(request):
    return render(request, "shop/index.html")


def checkout(request):
    return render(request, "shop/index.html")