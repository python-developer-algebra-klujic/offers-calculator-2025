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

    def __str__(self):
        return f'Ingredient: {self.name}'