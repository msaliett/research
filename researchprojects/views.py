from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hola món!")

# Create your views here.
