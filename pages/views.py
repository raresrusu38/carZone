from django.shortcuts import render
from pages.models import Teams
from cars.models import *


def home(request):
    teams = Teams.objects.all().order_by('-id')
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    latest_cars = Car.objects.all().order_by('-created_date')
    model_search = Car.objects.order_by().values('model').distinct()
    city_search = Car.objects.order_by().values('city').distinct()
    year_search = Car.objects.order_by().values('year').distinct()
    body_style_search = Car.objects.order_by().values('body_style').distinct()
    
    context = {
        'teams' : teams,
        'featured_cars' : featured_cars,
        'latest_cars' : latest_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'pages/home.html', context)


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
