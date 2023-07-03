from rest_framework import serializers
from django.core.validators import RegexValidator

from restaurant.models import Restaurant, Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ("date", "items")

    def create(self, validated_data):
        return Menu.objects.create(**validated_data)


class RestaurantSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    menu = MenuSerializer(many=False, read_only=True)

    contact_number = serializers.CharField(
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message='Contact number must be in the format: "+999999999". Up to 15 digits allowed.',
            )
        ]
    )

    class Meta:
        model = Restaurant
        fields = (
            "name",
            "address",
            "contact_number",
            "email",
            "description",
            "menu",
            "website",
            "capacity",
            "cuisine_type",
            "owner",
            "menu",
        )
        read_only_fields = ("id", "owner")

    def get_owner(self, obj):
        return obj.owner.first_name + " " + obj.owner.last_name

    def create(self, validated_data):
        request = self.context.get("request")
        owner = request.user if request else None
        restaurant = Restaurant.objects.create(owner=owner, **validated_data)

        return restaurant


class DetailMenuSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ("date", "items", "restaurant_name")
        ordering = ["restaurant__name"]

    def get_restaurant_name(self, obj):
        return obj.restaurant.name
