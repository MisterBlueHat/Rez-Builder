from django.shortcuts import render, HttpResponse
from django.template import loader
from myapp.scripts.yelp import response
from myapp.models import Restaurant
from .forms import InputForm 

import random
import requests
import json

# Create your views here.
def home(request):
	template = loader.get_template("templates/index.html")
	return HttpResponse(template.render())

def filter(request):
	if request.POST:
		context ={
		'form' : InputForm(),
		'restaurants' : Restaurant.objects.all()
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
	rest_pick = Restaurant.get(pk=rest_id)
	context = {
		'rest_name': "Wendigo",
		'rest_city': "Stoughton",
		'rest_rating': 4.5,
		'rest_site': "https://www.yelp.com/biz/wendigo-stoughton?adjust_creative=EVUuU37E7M-yE3h-cridyw&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=EVUuU37E7M-yE3h-cridyw",
		'rest_phone': "(608) 205-2775",
		'rest_addr': "121 E Main St",
		'rest_img': "https://s3-media1.fl.yelpcdn.com/bphoto/ilbS7coMJaNsdneALh-PdA/o.jpg",
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

# views.py 

from .models import Restaurant

def restaurant_reviews(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    reviews = restaurant.Reviews(restaurant_id)
    
    reviews_data = reviews.get_reviews()
    
    context = {
        'reviews': reviews_data
    }
    
    return render(request, 'reviews.html', context)

def About(request):
	template = loader.get_template("templates/About.html")
	return HttpResponse(template.render())

def TOS(request):
	template = loader.get_template("templates/TOS.html")
	return HttpResponse(template.render())

def Contact(request):
	template = loader.get_template("templates/CONTACT.html")
	return HttpResponse(template.render())

