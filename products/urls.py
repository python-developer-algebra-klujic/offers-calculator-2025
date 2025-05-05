from django.urls import path
from . import views

urlpatterns = [
    path('ingredients/', views.ingredients_list, name='ingredients_list'),
    path('ingredients/db-seed/', views.ingredients_seeder, name='db_seed'),
    path('ingredients/add/', views.ingredient_add, name='ingredient_add'),
    path('ingredients/edit/<int:pk>', views.ingredient_edit, name='ingredient_edit'),
    path('ingredients/<int:pk>', views.ingredient_details, name='ingredient_details'),
    path('', views.ingredients_list, name='home'),
]