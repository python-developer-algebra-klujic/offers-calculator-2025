from django.urls import path

from .views import IngredientListView, ProductListView
from . import views

urlpatterns = [
    path('ingredients/', IngredientListView.as_view(), name='ingredients_list'),
    path('ingredients/db-seed/', views.ingredients_seeder, name='db_seed'),
    path('ingredients/add/', views.ingredient_add, name='ingredient_add'),
    path('ingredients/edit/<int:pk>', views.ingredient_edit, name='ingredient_edit'),
    path('ingredients/<int:pk>', views.ingredient_details, name='ingredient_details'),

    path('<int:pk>', views.product_details, name='product_details'),
    path('add/', views.products_add, name='product_add'),
    path('', ProductListView.as_view(), name='home'),
]