from django.db import models

class Restaurant(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    site = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    image = models.CharField(max_length=100)