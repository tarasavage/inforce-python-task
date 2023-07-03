from django.urls import path

from authentication.views import CreateUserView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="register"),
]

app_name = "authentication"
