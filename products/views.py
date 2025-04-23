from django.shortcuts import render

# Create your views here.
def ingredients_list(request):
    return render(request, 'products/ingredients.html')
