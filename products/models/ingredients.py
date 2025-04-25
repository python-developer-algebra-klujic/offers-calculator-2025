from decimal import Decimal
from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=150,
                            help_text='Ingredient name',
                            null=False,
                            blank=False)
    code = models.CharField(max_length=10,
                            help_text='Ingredient code',
                            null=False,
                            blank=False)
    description = models.CharField(max_length=500,
                            help_text='Ingredient description',
                            null=True,
                            blank=True)
    base_price = models.DecimalField(max_digits=18,
                                     decimal_places=6,
                                     default=Decimal('1.00'),
                                     help_text='Ingredient base price',
                                     null=True,
                                     blank=True)
    price_mod = models.DecimalField(max_digits=5,
                                     decimal_places=3,
                                     default=Decimal('1.00'),
                                     help_text='Ingredient price modification index',
                                     null=True,
                                     blank=True)
    final_price = models.DecimalField(max_digits=18,
                                     decimal_places=6,
                                     default=Decimal('1.00'),
                                     help_text='Ingredient final price',
                                     null=True,
                                     blank=True)

    def __str__(self):
        return f'Ingredient: {self.name} ({self.code})'
