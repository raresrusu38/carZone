from django.shortcuts import render
from pages.models import Teams



def home(request):
    teams = Teams.objects.all().order_by('-id')
    data = {
        'teams' : teams,
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
