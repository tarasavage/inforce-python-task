from datetime import date

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.serializers import UserSerializer
from restaurant.models import Restaurant, Menu


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class AddVoteView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, restaurant_id):
        try:
            restaurant = Restaurant.objects.get(id=restaurant_id)
            today = date.today()
            menu = restaurant.menus.get(date=today)
            menu.votes += 1
            menu.save()
            return Response(
                {"message": "Vote added successfully."}, status=status.HTTP_200_OK
            )
        except Restaurant.DoesNotExist:
            return Response(
                {"message": "Restaurant not found."}, status=status.HTTP_404_NOT_FOUND
            )


class HighestVotedView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request):
        try:
            menu = Menu.objects.order_by("-votes").first()

            if not menu:
                return Response(
                    {"message": "No highest voted menu found."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            data = {
                "id": menu.id,
                "date": menu.date,
                "items": menu.items,
                "votes": menu.votes,
            }

            # we need to set all votes to zero, because the next day
            # we will have another voting
            for menu_obj in Menu.objects.all():
                menu_obj.votes = 0
                menu_obj.save()

            return Response(data, status=status.HTTP_200_OK)
        except Menu.DoesNotExist:
            return Response(
                {"message": "Error retrieving highest voted menu."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
