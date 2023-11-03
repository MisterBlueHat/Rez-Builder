from django.urls import path
from . import views

urlpatterns = [
	path("home/", views.home, name="home"),
	path("landing/", views.landing, name="landing"),
	path("landing_test/", views.landing_test, name="landing_test"),
	path("filter/", views.filter, name="filter"),
    path("var_test/", views.var_test, name="var_test"),
    path("Index1/", views.Index1, name="index")
]