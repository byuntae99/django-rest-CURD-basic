from django.shortcuts import render
from django.http import HttpResponse
from .models import *




# Create your views here.
def home(request):
    return render(request,'home.html')

def data(request):
    name = request.POST['nameofperson']
    age = request.POST['age']
    obj = Room.objects.create(Name=name,Age=age)
    return HttpResponse("<h1>Created</h1>")
