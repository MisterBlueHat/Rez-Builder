from django.shortcuts import render, HttpResponse
from django.template import loader
from myapp.scripts.yelp import response
from .forms import InputForm 

import random
import requests
import json

loaded_restaurants = {}

# Create your views here.

def home(request):
	template = loader.get_template("templates/index.html")
	return HttpResponse(template.render())

def filter(request):
	context ={
		'form' : InputForm(),
		'restaurants' : response()
	}
	loaded_restaurants = context['restaurants']
	template = loader.get_template("templates/filter.html")	
	data = {request.POST.get('zip_code'), request.POST.get('max_distance'), request.POST.get('cuisine')}
	print(data)
    # Check if you get the value
	return HttpResponse(template.render(context, request))

def landing(request):
	template = loader.get_template("templates/landing.html")
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
