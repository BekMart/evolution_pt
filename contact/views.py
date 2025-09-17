from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def contact_page(request):
    return HttpResponse("Get in touch with us")
