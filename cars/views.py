from django.shortcuts import render, get_object_or_404
from cars.models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def cars(request):
    cars = Car.objects.all().order_by('-created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    page_cars = paginator.get_page(page)
    context = {
        'cars': page_cars,
    }
    return render(request, 'cars/cars.html', context)

def car_detail(request, pk, slug):
    single_car = get_object_or_404(Car, pk=pk, slug=slug)
    context = {
        'single_car' : single_car,
    }
    return render(request, 'cars/car-detail.html', context)
