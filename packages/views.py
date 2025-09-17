from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def packages_list(request):
    return HttpResponse("List of packages")
