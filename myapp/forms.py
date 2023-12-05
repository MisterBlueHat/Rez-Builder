from django import forms

food_choices = [
		("Italian", "Italian"),
		("Mexican", "Mexican"),
		("Chinese", "Chinese"),
		("Greek", "Greek"),
		("Spanish", "Spanish"),
		("Thai", "Thai"),
		("American", "American"),
	]

class InputForm(forms.Form):  
	city = forms.CharField(max_length = 200)  
	max_distance = forms.IntegerField()  
	cuisine= forms.CharField(label='Select cuisine', widget=forms.Select(choices=food_choices))
    