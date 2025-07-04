from django.shortcuts import render
from django.http import HttpResponse as htr

# Create your views here.
def index(request):
    return htr("this is poll app Home!!!")
