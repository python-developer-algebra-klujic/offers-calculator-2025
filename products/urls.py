from django.urls import path
from . import views

urlpatterns = [
    path('ingredients/', views.ingredients_list, name='ingredients_list'),
    path('ingredients/<int:pk>', views.ingredient_details, name='ingredient_details'),
    path('', views.ingredients_list, name='home'),
]