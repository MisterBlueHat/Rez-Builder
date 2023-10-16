from django.shortcuts import render, HttpResponse
from myapp.scripts.yelp import response

import requests
import json

# Create your views here.

def home(request):
	return HttpResponse("Home")

def filter(request):
	return HttpResponse(response())

def landing(request):
	return HttpResponse("Landing")
