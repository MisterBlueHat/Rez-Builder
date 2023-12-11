from django.shortcuts import render, HttpResponse
from django.template import loader
from myapp.scripts.yelp import response
from myapp.scripts.reviews import response as review_response
from myapp.models import Restaurant
from .forms import InputForm 
from django.core.paginator import Paginator

import random
import requests
import json

# Create your views here.
def home(request):
	template = loader.get_template("templates/index.html")
	return HttpResponse(template.render())

def filter(request):
	if request.POST:
		Restaurant.objects.all().delete()
		response(request.POST.get('city'), request.POST.get('max_distance'), request.POST.get('price'))
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
	rest_pick = Restaurant.objects.get(pk=rest_id)
	review = review_response(rest_id)
	print(review)
	context = {
		'rest_name': rest_pick.name,
		'rest_city': rest_pick.city,
		'rest_rating': rest_pick.rating,
		'rest_site': rest_pick.site,
		'rest_phone': rest_pick.phone,
		'rest_addr': rest_pick.address,
		'rest_img': rest_pick.image,
		'rest_reviews' : review
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
'''
from .models import Restaurant

def restaurant_reviews(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    reviews = restaurant.Reviews(restaurant_id)
    
    reviews_data = reviews.get_reviews()
    
    context = {
        'reviews': reviews_data
    }
    
    return render(request, 'reviews.html', context)
'''
def About(request):
	template = loader.get_template("templates/About.html")
	return HttpResponse(template.render())

def TOS(request):
	template = loader.get_template("templates/TOS.html")
	return HttpResponse(template.render())

def Contact(request):
	template = loader.get_template("templates/CONTACT.html")
	return HttpResponse(template.render())

def restaurant_detail(request, id):

    reviews = Restaurant.objects.get(id=id).review_set.all()  

    page_num = request.GET.get('page', 1)
    p = Paginator(reviews, 5) # 5 reviews per page
    page = p.page(page_num)

    context = {'page': page}
    return render(request, 'detail.html', context)

def landing_object(request):
    restaurants = Restaurant.objects.all() 
    return render(request, 'landing.html', {'restaurants': restaurants})

'''
def landing(request):
    restaurant = Restaurant.objects.get(pk=1) 
    return render(request, 'landing.html', {'reviews': restaurant.reviews.all()})
'''
