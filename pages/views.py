from django.shortcuts import render, redirect
from pages.models import Teams
from cars.models import *
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages


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
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = "You have a new message from CarZone website regarding " + subject
        message_body = "Name: " + name + ". Email: " + email + ". Phone: " + phone + ". message: " + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
            email_subject,
            message_body,
            'rares.rusu29@gmail.com',
            [admin_email],
            fail_silently=False,
        )
        messages.success(request, "Thank you for contacting us, we will get back to you shortly")
        return redirect('pages:contact')

    return render(request, 'pages/contact.html')
