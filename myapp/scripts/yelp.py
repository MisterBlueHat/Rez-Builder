import requests
import json
from myapp.scripts.restaurant import Restaurant as res 
from myapp.models import Restaurant 

headers = {
    "accept": "application/json",
    "Authorization": 'Bearer GTqVWtOkg5Wx8XtcLeNoSmmv06jZ-gicMXW_mSfLD2ALgj3OL6jW300b9m3lOaIhoDLcMdSMdExM3vOJAgqwGiwiKtRpcD-7Y-3lyjSEF7Jzk3bGeSEwn0tS9xNAZXYx'
}

def setParams(city, max_distance, price):
    #Parameters for restaurant selection
    url = "https://api.yelp.com/v3/businesses/search?sort_by=best_match&limit=20"
    parameters = {
        "location": city,
        "latitude": "",
        "longitude": "",
        "term": "",
        "radius": max_distance,
        "categories": "",
        "locale": "",
        "price": price,
    }
    for param in parameters:
        if parameters[param] != "":
            url = url + "&" + param + "=" + parameters[param]
    print(url)
    return url

def response(city, max_distance, price):
    url = setParams(city, str(int(max_distance) * 1609), price)
    response = requests.get(url, headers=headers).json()
    
    for r in response["businesses"]:
        restaurant = Restaurant(
            id=r["id"], 
            name=r["name"], 
            city=r["location"]["city"], 
            rating=r["rating"], 
            site=r["url"], 
            phone=r["display_phone"], 
            address=r["location"]["address1"], 
            image=r["image_url"]
            )
        restaurant.save()

#Create a text file if it doesn't already exist and write the the fetched JSON to it. 
#with open('response.json', 'w') as f: json.dump(response.json(), f, indent="\t")
