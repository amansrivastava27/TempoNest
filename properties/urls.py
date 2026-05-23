from django.urls import path
from . import views

urlpatterns = [

    path('add/',
         views.add_property,
         name='add_property'),

    path('my-properties/',
         views.my_properties,
         name='my_properties'),

    path(
    'detail/<int:id>/',
    views.property_detail,
    name='property_detail'),

]