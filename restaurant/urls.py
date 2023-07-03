from django.urls import path

from restaurant.views import CreateRestaurantView

urlpatterns = [
    path("create/", CreateRestaurantView.as_view(), name="create"),
]

app_name = "restaurant"
