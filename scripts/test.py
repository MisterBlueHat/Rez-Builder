import requests
import json

url = "https://api.yelp.com/v3/businesses/search?sort_by=best_match&limit=20"

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

for param in parameters:
    if parameters[param] != "":
        url = url + "&" + param + "=" + parameters[param]

print(url,"/n")

headers = {
    "accept": "application/json",
    "Authorization": 'Bearer FoZr_sHH0IZ981_y58GdqRaLaKIzIc76HJuXhxbspj6oG8_Sd_Inx7WoFptaTjAitdmCpxLougxgzASnvpc9CgaRNhLsf0x3uWkkaUIDxlQHIGUC95e6JEqsJp8PZXYx'
}

response = requests.get(url, headers=headers)

with open('response.json', 'w') as f: json.dump(response.json(), f, indent="\t")
