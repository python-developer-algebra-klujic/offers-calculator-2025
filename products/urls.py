from django.urls import path
from . import views

urlpatterns = [
    path('ingredients/', views.ingredients_list, name='ingredients_list'),
    path('ingredients/add/', views.ingredient_add, name='ingredient_add'),
    path('ingredients/<int:pk>', views.ingredient_details, name='ingredient_details'),
    path('', views.ingredients_list, name='home'),
]