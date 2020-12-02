from django.urls import path
from contacts.views import *
from contacts import views

app_name = "contacts"

urlpatterns = [
    path('inquiry', views.inquiry,  name="inquiry"),
]
