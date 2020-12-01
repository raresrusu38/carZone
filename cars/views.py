from django.shortcuts import render, get_object_or_404
from cars.models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def cars(request):
    cars = Car.objects.all().order_by('-created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    page_cars = paginator.get_page(page)

    model_search = Car.objects.order_by().values('model').distinct()
    city_search = Car.objects.order_by().values('city').distinct()
    year_search = Car.objects.order_by().values('year').distinct()
    body_style_search = Car.objects.order_by().values('body_style').distinct()

    context = {
        'cars': page_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'cars/cars.html', context)

def car_detail(request, pk, slug):
    single_car = get_object_or_404(Car, pk=pk, slug=slug)
    context = {
        'single_car' : single_car,
    }
    return render(request, 'cars/car-detail.html', context)

def search(request):
    cars = Car.objects.order_by('-created_date')

    model_search = Car.objects.order_by().values('model').distinct()
    city_search = Car.objects.order_by().values('city').distinct()
    year_search = Car.objects.order_by().values('year').distinct()
    body_style_search = Car.objects.order_by().values('body_style').distinct()
    transmition_search = Car.objects.order_by().values('transmition').distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'transmition' in request.GET:
        transmition = request.GET['transmition']
        if transmition:
            cars = cars.filter(transmition__iexact=transmition)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    context = {
        'cars' : cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmition_search': transmition_search,
    }

    return render(request, 'cars/search.html', context)
