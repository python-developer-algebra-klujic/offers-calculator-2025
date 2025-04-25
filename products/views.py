from django.shortcuts import render, get_object_or_404
from .models import Ingredient

# Create your views here.
def ingredients_list(request):
    # Dohvat podataka iz baze
    ingredients = Ingredient.objects.all()

    return render(request,
                  'products/ingredients.html',
                  {'ingredients': ingredients})


def ingredient_details(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)

    return render(request,
                  'products/ingredient-details.html',
                  {'ingredient': ingredient})
