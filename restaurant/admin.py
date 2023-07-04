from django.contrib import admin
from .models import Restaurant, Menu


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "owner")


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("restaurant", "date", "votes")
