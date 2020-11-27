from django.urls import path
from cars.views import *
from cars import views

app_name = "cars"

urlpatterns = [
    path('', views.cars, name="cars"),
]
