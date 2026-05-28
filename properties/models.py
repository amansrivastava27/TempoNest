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
    
class Booking(models.Model):

    STATUS_CHOICES = (

        ('Pending', 'Pending'),

        ('Accepted', 'Accepted'),

        ('Rejected', 'Rejected'),

    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE
    )

    phone = models.CharField(
        max_length=15
    )

    message = models.TextField()

    booked_at = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):

        return f"{self.user.username} booked {self.property.title}"
    

class PropertyImage(models.Model):

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='gallery'
    )

    image = models.ImageField(
        upload_to='property_gallery/'
    )

    def __str__(self):

        return self.property.title


class Payment(models.Model):

    booking = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE
    )

    razorpay_order_id = models.CharField(
        max_length=200
    )

    razorpay_payment_id = models.CharField(
        max_length=200
    )

    razorpay_signature = models.CharField(
        max_length=500
    )

    amount = models.IntegerField()

    paid = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.razorpay_payment_id