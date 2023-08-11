from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("HELLO WORLD")

def abc(request):
    return HttpResponse("PYTHON DJANGO")