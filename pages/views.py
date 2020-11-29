from django.shortcuts import render
from pages.models import Teams
from cars.models import *


def home(request):
    teams = Teams.objects.all().order_by('-id')
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    latest_cars = Car.objects.all().order_by('-created_date')
    data = {
        'teams' : teams,
        'featured_cars' : featured_cars,
        'latest_cars' : latest_cars
    }
    return render(request, 'pages/home.html', data)


def about(request):
    teams = Teams.objects.all().order_by('-id')
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')
