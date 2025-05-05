from django.contrib import admin

from .models import (Product,
                     Ingredient)

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Product)
