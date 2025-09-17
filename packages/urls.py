from django.urls import path
from . import views


# Define URL patterns for the packages app
urlpatterns = [
    path('', views.packages_list, name='packages-list'),
]
