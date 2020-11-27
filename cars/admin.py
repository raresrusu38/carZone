from django.contrib import admin
from cars.models import *


class CarAdmin(admin.ModelAdmin):
    list_display = ('car_title',)


admin.site.register(Car, CarAdmin)
