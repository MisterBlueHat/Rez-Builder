from django.shortcuts import render, HttpResponse
from django.template import loader
from myapp.scripts.yelp import response, detailed_response
from .forms import InputForm 

import random
import requests
import json

loaded_restaurants = {}
# Create your views here.
# This is a test to make sure commits work
def home(request):
	template = loader.get_template("templates/index.html")
	return HttpResponse(template.render())

def filter(request):
	if request.POST:
		loaded_restaurants = response(request.POST.get('city'))
		context ={
		'form' : InputForm(),
		'restaurants' : loaded_restaurants
		}
	else:
		context ={
		'form' : InputForm(),
		}
	template = loader.get_template("templates/filter.html")	
    # Check if you get the value
	return HttpResponse(template.render(context, request))

def landing(request):
	template = loader.get_template("templates/landing.html")
	rest_id = request.GET.get('id', '')
	print(rest_id)
	rest = detailed_response(rest_id)
	context = {
		'rest_id': rest_id,
		'rest_city': rest["location"]["city"],
		'rest_rating': rest["rating"],
		'rest_site': rest["url"],
		'rest_phone': rest["phone"],
		'rest_addr': rest["location"]["address1"],
		'rest_img': rest["image_url"],
		'rest_lat': rest["coordinates"]["latitude"],
		'rest_lon': rest["coordinates"]["longitude"],
	}
	return HttpResponse(template.render(context,request))

def landing_test(request):
	template = loader.get_template("templates/landing_test.html")
	context = {
		'rest_name': request.GET.get('name', ''),
		'rest_city': request.GET.get('city', ''),
		'rest_rating': request.GET.get('rating', ''),
		'rest_site': request.GET.get('site', ''),
		'rest_phone': request.GET.get('phone', ''),
		'rest_addr': request.GET.get('addr', ''),
		'rest_img': request.GET.get('img', ''),
	}
	return HttpResponse(template.render(context, request))

def var_test(request):
	template = loader.get_template("templates/var_test.html")
	return HttpResponse(template.render(request))
