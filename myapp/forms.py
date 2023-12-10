from django import forms

food_choices = [
		(1, "$"),
		(2, "$$"),
		(3, "$$$"),
		(4, "$$$$"),
	]

class InputForm(forms.Form):  
	city = forms.CharField(max_length = 200)  
	max_distance = forms.IntegerField()  
	price= forms.IntegerField(label='Select Price:', widget=forms.Select(choices=food_choices))
    