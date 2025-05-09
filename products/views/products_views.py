from django.views.generic import ListView
from django.shortcuts import redirect, render, get_object_or_404

from ..models import Product, Ingredient


class ProductListView(ListView):
    model = Product
    paginate_by = 5


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request,
                  'products/product-details.html',
                  {'product': product})


def products_add(request):
    if request.method == 'POST':
        product = Product.objects.create(
            name = request.POST.get('name'),
            code = request.POST.get('code'),
            description = request.POST.get('description'),
            base_price = request.POST.get('base_price') or 1,
            fixed_costs = request.POST.get('fixed_costs') or 1,
            price_mod = request.POST.get('price_mod') or 1,
            final_price = request.POST.get('final_price') or 1
        )

        product.ingredients.set(request.POST.getlist('ingredients'))
        product.ingredients_from_products.set(request.POST.getlist('ingredients_from_products'))

        product.save()

        return redirect('products:home')

    ingredients = Ingredient.objects.all()
    ingredients_from_products = Product.objects.all()

    return render(request,
                  'products/product-form.html',
                  {
                      "ingredients_list": ingredients,
                      "ingredients_from_products_list": ingredients_from_products
                })
