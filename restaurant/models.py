from datetime import datetime

from django.db import models
from django.template.defaultfilters import slugify
from rest_framework.authtoken.admin import User


class Restaurant(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    rating = models.SmallIntegerField(default=5)

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    dishes = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f'{self.restaurant} - {self.date}'


class Employee(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return f'{self.employee}'


class Vote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return f'{self.employee} - {self.restaurant}'


