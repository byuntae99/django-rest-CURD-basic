
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('data/',views.data,name="data")
]
