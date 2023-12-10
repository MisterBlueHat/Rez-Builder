# restaurant_request.py
import requests
import json
from django.db import models
import base64

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    # Add other fields as needed such as zip code and price range

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_rating(self):
        return self.rating

    def get_location(self):
        return self.address

    def get_reviews(self):
        # Implement your own logic to retrieve reviews from a review platform
        return "No reviews yet"

    reviews = models.ManyToManyField(Review)

    def get_reviews_by_id(business_id, api_key):
        url = f"https://api.yelp.com/v3/businesses/{business_id}/reviews"

        headers = {
            "Authorization": f"Bearer {api_key}"
        }    

        response = requests.get(url, headers=headers)
        reviews = response.json()["reviews"]

    return reviews

        response = requests.get(url, headers=headers, params=params)

        # Get reviews
        yelp_reviews = response.json()['reviews']
    
        for review in yelp_reviews:
        # Create Review object for each
        Review.objects.create(
            text=review['text'],
            rating=review['rating'],
            restaurant=restaurant  
        )

        if response.status_code == 200:
            data = response.json()
            businesses = data.get("businesses", [])

            for business in businesses:
                name = business.get("name", "N/A")
                rating = business.get("rating", "N/A")
                address = business.get("location", {}).get("address1", "N/A")

                print(f"Name: {name}")
                print(f"Rating: {rating}")
                print(f"Address: {address}")
                print("\n")

        else:
            print(f"Error: {response.status_code} - {response.text}")

    if __name__ == "__main__":
        api_key = "UgaYzODUIn9ve-se0d6J1eKoFFYNyrFtkBybJ0JDJ1jeKNQG_6xOUN_BL30cleMd897fM4YF-wFCVq-Cf0PMOV8eeiAAZfbkeO2F5W_DWHaTY1YvSU5VjlJq2Ss4ZXYx"
        location = "Boston" # I added a location to perform search query results
        search_restaurants(location, api_key) # This function will perform search query results

class Review(models.Model):
    text = models.TextField()
    rating = models.IntegerField() 
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
        
logger = logging.getLogger(__name__)

def landing(request):
    try:
        # Error handling code to display landing page
        return render(request, 'landing.html')
    except Exception as e:
        logger.error("Error loading landing page", exc_info=True)
        return HttpResponseServerError("Oops, something went wrong. Please try again later.")
