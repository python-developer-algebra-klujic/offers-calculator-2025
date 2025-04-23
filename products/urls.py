from django.urls import path
from . import views

urlpatterns = [
    path('ingredients/', views.ingredients_list, name='ingredients_list'),
    path('', views.ingredients_list, name='home'),
]