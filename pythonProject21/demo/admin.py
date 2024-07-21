from django.contrib import admin

# Register your models here.
from .models import Person, Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'model','color']
    list_filter = ['brand','model']

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'car']
