from django.db import models
from django.contrib.auth.models import User


CATEGORY_CHOICES = (

    ('rooms', 'Rooms'),

    ('pg', 'PG'),

    ('flats', 'Flats'),

    ('houses', 'Houses'),

    ('hostels', 'Hostels'),

)


class Property(models.Model):

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    price = models.IntegerField()

    location = models.CharField(max_length=200)

    city = models.CharField(
        max_length=100,
        default='Unknown'
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to='properties/'
    )

    available = models.BooleanField(default=True)

    wifi = models.BooleanField(default=False)

    parking = models.BooleanField(default=False)

    food = models.BooleanField(default=False)

    ac = models.BooleanField(default=False)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.title