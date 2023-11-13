import requests
import json
from myapp.scripts.restaurant import Restaurant as res 

url = "https://api.yelp.com/v3/businesses/search?sort_by=best_match&limit=20"

#Parameters for restaurant selection
parameters = {
    "location": "Boston",
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
    "Authorization": 'Bearer GTqVWtOkg5Wx8XtcLeNoSmmv06jZ-gicMXW_mSfLD2ALgj3OL6jW300b9m3lOaIhoDLcMdSMdExM3vOJAgqwGiwiKtRpcD-7Y-3lyjSEF7Jzk3bGeSEwn0tS9xNAZXYx'
}

#Fetch a response from the Yelp API

def response():
    response_table = []
    response = requests.get(url, headers=headers).json()
    for r in response["businesses"]:
       response_table.append(res(r["name"], r["location"]["city"], r["rating"], r["id"],  r["url"], r["display_phone"], r["location"]["address1"], r["image_url"]))
    return response_table

#Create a text file if it doesn't already exist and write the the fetched JSON to it. 
#with open('response.json', 'w') as f: json.dump(response.json(), f, indent="\t")
