from django.shortcuts import render, redirect
from pages.views import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib import auth
from django.contrib.auth import authenticate
from contacts.models import *
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        firstname           = request.POST['firstname']
        lastname            = request.POST['lastname']
        username            = request.POST['username']
        email               = request.POST['email']
        password            = request.POST['password']
        confirm_password    = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email already exists')
                    return redirect('accounts:register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    auth_login(request, user)
                    messages.success(request, 'You are now logged in')
                    return redirect('accounts:dashboard')
                    user.save()
                    messages.success(request, 'You are registered successfully')
                    return redirect('accounts:login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('accounts:register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('accounts:login')
    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('pages:home')
    return redirect('pages:home')

@login_required(login_url='accounts:login')
def dashboard(request):
    user_inquiry = Contact.objects.order_by('-create_date').filter(user_id=request.user.id)

    context = {
        'inquiries' : user_inquiry,
    }

    return render(request, 'accounts/dashboard.html', context)
