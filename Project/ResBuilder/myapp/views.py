from django.shortcuts import render, HttpResponse
from django.template import loader
from myapp.scripts.yelp import response
from .forms import InputForm 

import random
import requests
import json

# Create your views here.

def home(request):
	template = loader.get_template("templates/index.html")
	return HttpResponse(template.render())

def filter(request):
	context ={}
	context['form']= InputForm()
	template = loader.get_template("templates/filter.html")	
	data = {request.POST.get('zip_code'), request.POST.get('max_distance'), request.POST.get('cuisine')}
	print(data)
    # Check if you get the value
	return HttpResponse(template.render(context, request))

def landing(request):
	template = loader.get_template("templates/landing.html")
	context = {
		'rest_name': "Wendigo",
		'rest_city': "Stoughton",
		'rest_rating': 4.5,
		'rest_site': "https://www.yelp.com/biz/wendigo-stoughton?adjust_creative=EVUuU37E7M-yE3h-cridyw&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=EVUuU37E7M-yE3h-cridyw",
		'rest_phone': "(608) 205-2775",
		'rest_addr': "121 E Main St",
		'rest_img': "https://s3-media1.fl.yelpcdn.com/bphoto/ilbS7coMJaNsdneALh-PdA/o.jpg",
	}
	return HttpResponse(template.render(context, request))

def landing_test(request):
	template = loader.get_template("templates/landing_test.html")
	restaurant_pick = response()[random.randrange(len(response()))]
	context = {
		'rest_name': "Wendigo",
		'rest_city': "Stoughton",
		'rest_rating': 4.5,
		'rest_site': "https://www.yelp.com/biz/wendigo-stoughton?adjust_creative=EVUuU37E7M-yE3h-cridyw&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=EVUuU37E7M-yE3h-cridyw",
		'rest_phone': "(608) 205-2775",
		'rest_addr': "121 E Main St",
		'rest_img': "https://s3-media1.fl.yelpcdn.com/bphoto/ilbS7coMJaNsdneALh-PdA/o.jpg",
	}
	return HttpResponse(template.render(context, request))

def var_test(request):
	template = loader.get_template("templates/var_test.html")
	restaurant_pick = response()[random.randrange(len(response()))]
	context = {
		'rest_name': restaurant_pick.name,
		'rest_city': restaurant_pick.city,
		'rest_rating': restaurant_pick.rating,
	}
	return HttpResponse(template.render(context, request))
