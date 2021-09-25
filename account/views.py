from django.shortcuts import render

from django.http import HttpResponse
def dashboard(request):
    return HttpResponse('Dashboard page')

def contact(request):
    return HttpResponse("Contact page")

# Create your views here.
