from django.urls import path
from . import views


# this file does not need preceding slashes in the routes

urlpatterns = [
    path('', views.index),
    path('about', views.hello),
    path('contact', views.contact),
    path('success', views.success)
]   