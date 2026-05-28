from django.urls import path
from . import views

urlpatterns = [

    path('add/',
         views.add_property,
         name='add_property'),

     path(
    'edit/<int:property_id>/',
    views.edit_property,
    name='edit_property'),

     path(
    'delete/<int:property_id>/',
    views.delete_property,
    name='delete_property'),

    path('my-properties/',
         views.my_properties,
         name='my_properties'),

    path(
    'detail/<int:id>/',
    views.property_detail,
    name='property_detail'),

    path(
    'book/<int:id>/',
    views.book_property,
    name='book_property'),

    path(
    'owner-bookings/',
    views.owner_bookings,
    name='owner_bookings'),
    path(
    'accept-booking/<int:id>/',
    views.accept_booking,
    name='accept_booking'),

    path(
    'reject-booking/<int:id>/',
    views.reject_booking,
    name='reject_booking'),

    path(
    'owner-dashboard/',
    views.owner_dashboard,
    name='owner_dashboard'),

    path(
    'payment/<int:booking_id>/',
    views.payment_page,
    name='payment_page'),

    path(
    'payment-success/',
    views.payment_success,
    name='payment_success'),


]