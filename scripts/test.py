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
response = requests.get(url, headers=headers)

#Create a text file if it doesn't already exist and write the the fetched JSON to it. 
with open('response.json', 'w') as f: json.dump(response.json(), f, indent="\t")
