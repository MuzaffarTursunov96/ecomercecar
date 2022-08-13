from django.urls import path,include
from .views import *

urlpatterns = [    
    # path('carlist', CarsAPi.as_view(),name='home'),
    path('cars', CarListAPI.as_view(),name='listApI'),
]
