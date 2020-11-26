from django.urls import path
from .views import *
from pages import views

app_name = "pages"

urlpatterns = [
    path('', views.home, name="home"),
]
