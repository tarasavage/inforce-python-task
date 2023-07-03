from django.urls import path

from authentication.views import AddVoteView, HighestVotedView
from restaurant.views import CreateRestaurantView, CreateMenuView, ListMenuView

urlpatterns = [
    path("create/", CreateRestaurantView.as_view(), name="create"),
    path("menu/create/", CreateMenuView.as_view(), name="create-menu"),
    path("menu/list/", ListMenuView.as_view(), name="menu-list"),
    path(
        "<int:restaurant_id>/vote/",
        AddVoteView.as_view(),
        name="add-vote",
    ),
    path("menu/winner/", HighestVotedView.as_view(), name="menu-winner"),
]

app_name = "restaurant"
