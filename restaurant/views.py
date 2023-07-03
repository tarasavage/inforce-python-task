from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer


class CreateRestaurantView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
