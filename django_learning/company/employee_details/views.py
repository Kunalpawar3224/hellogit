from django.shortcuts import render
from django.http import HttpResponse
from employee_details.models import Employee

# Create your views here.

def details(request):
    return HttpResponse("You're looking good")