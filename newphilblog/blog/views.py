from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

def verify(request):
    return HttpResponse("google-site-verification: google3ce605377dd30bad.html")

def index(request):
    pass

def detail(request):
    pass
