from django.shortcuts import render, HttpResponse

import requests
import json



url = "https://api.yelp.com/v3/businesses/search?sort_by=best_match&limit=20"

#Parameters for restaurant selection
parameters = {
    "location": "Stoughton",
    "latitude": "",
    "longitude": "",
    "term": "",
    "radius": "",
    "categories": "",
    "locale": "",
    "price": "",
}

#Iterate through parameters and append them to the end of the URL
for param in parameters:
    if parameters[param] != "":
        url = url + "&" + param + "=" + parameters[param]

print(url,"/n")

headers = {
    "accept": "application/json",
    "Authorization": 'Bearer FoZr_sHH0IZ981_y58GdqRaLaKIzIc76HJuXhxbspj6oG8_Sd_Inx7WoFptaTjAitdmCpxLougxgzASnvpc9CgaRNhLsf0x3uWkkaUIDxlQHIGUC95e6JEqsJp8PZXYx'
}

#Fetch a response from the Yelp API

def response():
    response_string = ""
    response = requests.get(url, headers=headers).json()
    for restaurant in response["businesses"]:
       response_string += restaurant["name"] + "\n"
    return response_string

# Create your views here.

def home(request):
	return HttpResponse("Home")

def filter(request):
	return HttpResponse(response())

def landing(request):
	return HttpResponse("Landing")
