from django.contrib import admin

from restaurant.models import Menu, Restaurant, Employee, Vote

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Employee)
admin.site.register(Vote)
