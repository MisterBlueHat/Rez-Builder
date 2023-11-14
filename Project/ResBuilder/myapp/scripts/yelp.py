import requests
import json
from myapp.scripts.restaurant import Restaurant as res 

headers = {
    "accept": "application/json",
    "Authorization": 'Bearer GTqVWtOkg5Wx8XtcLeNoSmmv06jZ-gicMXW_mSfLD2ALgj3OL6jW300b9m3lOaIhoDLcMdSMdExM3vOJAgqwGiwiKtRpcD-7Y-3lyjSEF7Jzk3bGeSEwn0tS9xNAZXYx'
}

def setParams(city):
    #Parameters for restaurant selection
    url = "https://api.yelp.com/v3/businesses/search?sort_by=best_match&limit=20"
    parameters = {
        "location": city,
        "latitude": "",
        "longitude": "",
        "term": "",
        "radius": "",
        "categories": "",
        "locale": "",
        "price": "",
    }
    for param in parameters:
        if parameters[param] != "":
            url = url + "&" + param + "=" + parameters[param]
    return url

def response(city):
    url = setParams(city)
    response_table = {}
    response = requests.get(url, headers=headers).json()
    for r in response["businesses"]:
       response_table[r["id"]] = res(r["name"], r["location"]["city"], r["rating"], r["id"],  r["url"], r["display_phone"], r["location"]["address1"], r["image_url"], r["coordinates"])
    print(response_table)
    return response_table

def detailed_response(id):
    url = "https://api.yelp.com/v3/businesses/" + id
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer GTqVWtOkg5Wx8XtcLeNoSmmv06jZ-gicMXW_mSfLD2ALgj3OL6jW300b9m3lOaIhoDLcMdSMdExM3vOJAgqwGiwiKtRpcD-7Y-3lyjSEF7Jzk3bGeSEwn0tS9xNAZXYx"
    }
    return requests.get(url, headers=headers).json()

#Create a text file if it doesn't already exist and write the the fetched JSON to it. 
#with open('response.json', 'w') as f: json.dump(response.json(), f, indent="\t")
