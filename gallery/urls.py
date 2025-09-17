from django.urls import path
from . import views


# Define URL patterns for the gallery app
urlpatterns = [
    path('', views.gym_pictures, name='gym-pictures'),
]
