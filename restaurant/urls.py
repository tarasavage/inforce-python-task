from django.urls import path

from restaurant.views import CreateRestaurantView, CreateMenuView, ListMenuView

urlpatterns = [
    path("create/", CreateRestaurantView.as_view(), name="create"),
    path("menu/create/", CreateMenuView.as_view(), name="create_menu"),
    path("menu/list/", ListMenuView.as_view(), name="menu_list"),
]

app_name = "restaurant"
