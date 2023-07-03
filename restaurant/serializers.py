from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.core.validators import RegexValidator

from authentication.serializers import UserSerializer
from restaurant.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    contact_number = serializers.CharField(
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message='Contact number must be in the format: "+999999999". Up to 15 digits allowed.'
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
            "website",
            "capacity",
            "cuisine_type",
            "owner",
        )
        read_only_fields = ("id", "owner")

    def create(self, validated_data):
        request = self.context.get("request")
        owner = request.user if request else None
        restaurant = Restaurant.objects.create(owner=owner, **validated_data)

        return restaurant
