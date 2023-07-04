from datetime import date

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from restaurant.models import Menu, Restaurant
from restaurant.serializers import (
    RestaurantSerializer,
    MenuSerializer,
    DetailMenuSerializer,
)


class CreateRestaurantView(generics.CreateAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = (IsAuthenticated,)


class ListMenuView(generics.ListAPIView):
    serializer_class = DetailMenuSerializer

    def get_queryset(self):
        today = date.today()
        queryset = Menu.objects.filter(date=today)

        return queryset


class CreateMenuView(generics.CreateAPIView):
    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Restaurant.objects.filter(owner=user)

    def perform_create(self, serializer):
        restaurant = self.get_queryset().first()
        serializer.save(restaurant=restaurant)
