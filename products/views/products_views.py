from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404

from ..models import Product


def products_list(request):
    # Dohvat podataka iz baze
    products = Product.objects.all()
    paginator = Paginator(products, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'products/products.html', {"page_obj": page_obj})


def products_add(request):
    if request.method == 'POST':
        product = Product.objects.create(
            name = request.POST.get('name'),
            code = request.POST.get('code'),
            description = request.POST.get('description'),
            base_price = request.POST.get('base_price') or 1,
            fixed_costs = request.POST.get('fixed_costs') or 1,
            price_mod = request.POST.get('price_mod') or 1,
            final_price = request.POST.get('final_price') or 1,

            ingredients = request.POST.getlist('ingredients'),
            ingredients_from_products = request.POST.getlist('ingredients_from_products')
        )
        product.save()

        return redirect('products:home')

    return render(request, 'products/product-form.html')