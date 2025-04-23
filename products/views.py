from django.shortcuts import render
from .models import Ingredient

# Create your views here.
def ingredients_list(request):
    # Dohvat podataka iz baze
    ingredients = Ingredient.objects.all()

    return render(request,
                  'products/ingredients.html',
                  {'ingredients': ingredients})
