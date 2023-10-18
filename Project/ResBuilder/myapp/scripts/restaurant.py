class Restaurant ():

    def __init__(self, name, city, rating, id,):
        self.name = name
        self.city = city
        self.rating = rating
        self.id = id

    def __str__(self):
        return self.name
    

a = Restaurant("Cape Cod Pizza", "Brockton", 4.6, "aydtayit332du")

print(a)