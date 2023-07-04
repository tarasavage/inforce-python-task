import pytest
from datetime import date

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Restaurant, Menu
from restaurant.serializers import DetailMenuSerializer


@pytest.mark.django_db
class TestListMenuView:
    @pytest.fixture
    def api_client(self):
        return APIClient()

    def test_list_menu_view(self, api_client):
        user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        user.id = 1
        user.save()

        restaurant = Restaurant.objects.create(
            name="Restaurant 1",
            address="Address 1",
            contact_number="123456789",
            email="restaurant@example.com",
            description="Restaurant description",
            website="https://www.example.com",
            capacity=100,
            cuisine_type="Italian",
            owner=user,
        )

        menu1 = Menu.objects.create(
            restaurant=restaurant, date=date.today(), items="Menu 1 items", votes=0
        )

        url = reverse("restaurant:menu-list")
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK

        expected_data = DetailMenuSerializer([menu1], many=True).data
        assert response.data == expected_data


@pytest.mark.django_db
class TestCreateRestaurantView:
    @pytest.fixture
    def api_client(self):
        return APIClient()

    def test_create_restaurant_view(self, api_client):
        user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword",
            email="asdad@gmail.com",
            first_name="Adsda",
            last_name="asdasd",
        )
        api_client.force_authenticate(user=user)

        restaurant_data = {
            "name": "Restaurant 1",
            "address": "Address 1",
            "contact_number": "123456789",
            "email": "restaurant@example.com",
            "description": "Restaurant description",
            "website": "https://www.example.com",
            "capacity": 100,
            "cuisine_type": "Italian",
            "owner": user,
        }

        response = api_client.post("/api/restaurant/create/", data=restaurant_data)

        assert response.status_code == status.HTTP_201_CREATED

        assert response.data["name"] == restaurant_data["name"]
        assert response.data["address"] == restaurant_data["address"]

        assert Restaurant.objects.filter(name=restaurant_data["name"]).exists()
