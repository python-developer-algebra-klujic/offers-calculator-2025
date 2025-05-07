from decimal import Decimal
from django.db import models

from .ingredients import Ingredient


class Product(models.Model):
    name = models.CharField(max_length=150,
                            help_text='Product name',
                            default='No Product Name',
                            null=False,
                            blank=False)
    code = models.CharField(max_length=10,
                            help_text='Product code',
                            default='PPP-000',
                            null=False,
                            blank=False)
    description = models.CharField(max_length=500,
                            help_text='Product description',
                            null=True,
                            blank=True)
    base_price = models.DecimalField(max_digits=18,
                                     decimal_places=6,
                                     default=Decimal('1.00'),
                                     help_text='Product base price',
                                     null=True,
                                     blank=True)
    fixed_costs = models.DecimalField(max_digits=18,
                                     decimal_places=6,
                                     default=Decimal('1.00'),
                                     help_text='Product fixed production costs',
                                     null=True,
                                     blank=True)
    price_mod = models.DecimalField(max_digits=5,
                                     decimal_places=3,
                                     default=Decimal('1.00'),
                                     help_text='Product price modification index',
                                     null=True,
                                     blank=True)
    final_price = models.DecimalField(max_digits=18,
                                     decimal_places=6,
                                     default=Decimal('1.00'),
                                     help_text='Product final price',
                                     null=True,
                                     blank=True)
    ingredients = models.ManyToManyField(Ingredient,
                                         related_name='products',
                                         null=True,
                                         blank=True)
    ingredients_from_products = models.ManyToManyField('Product',
                                                       null=True,
                                                       blank=True)

    class Meta:
        # Sortiraj prvo po nazivu pa onda po kodu, ali kod silazno
        ordering = ['name', '-code']

    def __str__(self):
        return f'Product: {self.name} ({self.code})'
