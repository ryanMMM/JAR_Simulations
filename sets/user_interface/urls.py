from django.urls import path
from user_interface import views

urlpatterns = [
    path('', views.index, name='index'),
]
