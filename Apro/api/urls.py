from django.urls import path
from . import views

urlpatterns = [
    # path('',views.getRoutes),
    path('room/',views.list_od_data),
    path('room/<int:pk>',views.list_of_single),
    path('signup/',views.sign_up),
] 
