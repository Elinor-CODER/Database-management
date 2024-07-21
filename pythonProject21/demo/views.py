from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from demo.models import Car
from demo.models import Person
import random


def create_car(request):
    car = Car(
        brand=random.choice(['b1', 'b2', 'b3']),
        model=random.choice(['m1', 'm2', 'm3']),
        color=random.choice(['c1', 'c2', 'c3']),
    )
    car.save()
    return HttpResponse(f'GOOD! New car: {car.brand}, {car.model}')


def list_car(request):
    car_objects = Car.objects.filter(brand__contains='2')
    cars = [f'{c.id}:{c.brand}, {c.model}:{c.color} | {c.owners.all}' for c in car_objects]
    return HttpResponse('<br>'.join(cars))


def create_person(request):
    cars = Car.objects.all()
    for car in cars:
        Person.objects.create(name='P', car=car)
        return HttpResponse("Good goodniy")


def list_person(request):
    person_objects = Person.objects.all()
    people = [f'{p.name}: {p.car}' for p in person_objects]
    return HttpResponse('<br>'.join(people))
