from django.shortcuts import render, HttpResponse
from django.template import loader
from myapp.scripts.yelp import response
import random

import requests
import json

# Create your views here.

def home(request):
	return HttpResponse("Home")

def filter(request):
	return HttpResponse(response())

def landing(request):
	return HttpResponse("Landing")

def var_test(request):
	template = loader.get_template("templates/var_test.html")
	restaurant_pick = response()[random.randrange(len(response()))]
	context = {
		'rest_name': restaurant_pick.name,
		'rest_city': restaurant_pick.city,
		'rest_rating': restaurant_pick.rating,
	}
	return HttpResponse(template.render(context, request))
