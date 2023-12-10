import requests
import json

headers = {
    "accept": "application/json",
    "Authorization": 'Bearer GTqVWtOkg5Wx8XtcLeNoSmmv06jZ-gicMXW_mSfLD2ALgj3OL6jW300b9m3lOaIhoDLcMdSMdExM3vOJAgqwGiwiKtRpcD-7Y-3lyjSEF7Jzk3bGeSEwn0tS9xNAZXYx'
}

def response(id):
    url = "https://api.yelp.com/v3/businesses/" + id + "/reviews?limit=20&sort_by=yelp_sort"
    response = requests.get(url, headers=headers).json()
    
    for r in response["reviews"]:
        print(r["user"]["name"])
        
response("nvlxtOwbGqPW8E6_sYTfvw")

#Create a text file if it doesn't already exist and write the the fetched JSON to it. 
#with open('response.json', 'w') as f: json.dump(response.json(), f, indent="\t")
