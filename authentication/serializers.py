from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.utils.translation import gettext as _


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        label=_("Confirm Password"),
        style={"input_type": "password"},
        write_only=True,
        min_length=5
    )

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "password",
            "password2",
            "is_staff",
        )
        read_only_fields = ("id", "is_staff")
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def validate(self, attrs):
        password1 = attrs.get("password")
        password2 = attrs.get("password2")

        if password1 and password2 and password1 != password2:
            raise serializers.ValidationError(
                _("Passwords do not match."), code="password_mismatch"
            )

        return attrs

    def create(self, validated_data):
        validated_data.pop("password2", None)
        user = get_user_model().objects.create_user(**validated_data)
        return user
