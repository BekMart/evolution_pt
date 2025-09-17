from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def gym_pictures(request):
    return HttpResponse("Pictures of gym")
