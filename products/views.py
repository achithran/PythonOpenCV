from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Django!!")


def about(request):
    return HttpResponse("About us")