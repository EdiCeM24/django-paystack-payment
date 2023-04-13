from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('', views.initiate_payment, name='initiate-payment'),
    path('make-payment', views.make_payment, name='make-payment'),
]