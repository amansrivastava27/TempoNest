from django.urls import path
from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),

    path(
        'services/<str:category>/',
        views.services,
        name='services'
    ),

    path(
    'search/',
    views.search,
    name='search'
    ),

]