# Generated by Django 4.2.3 on 2023-07-03 18:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0002_alter_restaurant_owner_menu"),
    ]

    operations = [
        migrations.AddField(
            model_name="menu",
            name="votes",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
