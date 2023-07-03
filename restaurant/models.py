from django.contrib.auth import get_user_model
from django.db import models


class Restaurant(models.Model):
    name = models.CharField(
        max_length=255, unique=True, null=False, blank=False,
    )
    address = models.CharField(
        max_length=255, unique=True, null=False, blank=False,
    )
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()
    website = models.URLField()
    capacity = models.PositiveIntegerField()
    cuisine_type = models.CharField(max_length=100)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
