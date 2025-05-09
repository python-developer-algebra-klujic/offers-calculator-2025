from django.views.generic import ListView
from django.shortcuts import redirect, render, get_object_or_404

from ..models import ingredients_db_seed, Ingredient


class IngredientListView(ListView):
    model = Ingredient
    paginate_by = 5







def ingredient_details(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)

    return render(request,
                  'products/ingredient-details.html',
                  {'ingredient': ingredient})


def ingredient_edit(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)

    if request.method == 'POST':
        ingredient.name = request.POST.get('name'),
        ingredient.code = request.POST.get('code'),
        ingredient.description = request.POST.get('description'),
        ingredient.base_price = request.POST.get('base_price'),
        ingredient.price_mod = request.POST.get('price_mod'),
        ingredient.final_price = request.POST.get('final_price')
        ingredient.save()

        return redirect('products:ingredients_list')

    return render(request, 'products/ingredient-edit-form.html',
                  {'ingredient': ingredient})


def ingredient_add(request):
    if request.method == 'POST':
        ingredient = Ingredient.objects.create(
            name = request.POST.get('name'),
            code = request.POST.get('code'),
            description = request.POST.get('description'),
            base_price = request.POST.get('base_price') or 1,
            price_mod = request.POST.get('price_mod') or 1,
            final_price = request.POST.get('final_price') or 1
        )
        ingredient.save()

        return redirect('products:ingredients_list')

    return render(request, 'products/ingredient-form.html')


def ingredients_seeder(request):
    # seed database
    if request.method.GET:
        ingredients_db_seed()

    return redirect('products:ingredients_list')
