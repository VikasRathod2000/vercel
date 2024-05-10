from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),# data get from api
    path('api/data/', views.get_data, name='get_data'),# data upload 
    path('home/', views.home, name='home'),
    path('respond/', views.respond_to_message, name='respond_to_message'),
]
