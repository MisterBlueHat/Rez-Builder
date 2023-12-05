from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name="home"),
	path("landing/", views.landing, name="landing"),
	path("landing_test/", views.landing_test, name="landing_test"),
	path("filter/", views.filter, name="filter"),
    path("var_test/", views.var_test, name="var_test"),
    path("About/", views.About, name="About"),
    path("Contact/", views.Contact, name="Contact"),
    path("TOS/", views.TOS, name="TOS"),
]