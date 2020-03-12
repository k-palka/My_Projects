from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

# Create your views here.


def index(request):
    return HttpResponse("Hello world. You are in the offer index")


