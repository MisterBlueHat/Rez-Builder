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
		response(request.POST.get('city'))
		print(Restaurant.objects.all().values())
		context ={
		'form' : InputForm(),
		'restaurants' : request.session['loaded_restaurants']
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
	rest = request.session['loaded_restaurants'][rest_id]
	context = {
		'rest_id': rest_id,
		'rest_city': rest.city,
		'rest_rating': rest.rating,
		'rest_site': rest.site,
		'rest_phone': rest.phone,
		'rest_addr': rest.address,
		'rest_img': rest.image,
		'rest_lat': rest.lat,
		'rest_lon': rest.lon,
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
