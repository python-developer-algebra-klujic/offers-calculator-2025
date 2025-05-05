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
