from django.urls import path
from cars.views import *
from cars import views

app_name = "cars"

urlpatterns = [
    path('', views.cars, name="cars"),
    path('<int:pk>/<slug:slug>/', views.car_detail, name="car-detail"),
]
