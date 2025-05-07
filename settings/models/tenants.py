from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=250,
                            help_text='Tenant name',
                            null=False,
                            blank=False)
    vat_id = models.CharField(max_length=20,
                              help_text='Tenant VATID',
                              null=True,
                              blank=True)
    street_and_number = models.CharField(max_length=250,
                                         help_text='Tenant address street with number',
                                         null=True,
                                         blank=True)
    postal_number = models.CharField(max_length=50,
                                     help_text='Tenant address postal number',
                                     null=True,
                                     blank=True)
    city = models.CharField(max_length=150,
                            help_text='Tenant address city',
                            null=True,
                            blank=True)
    country = models.CharField(max_length=150,
                               help_text='Tenant address country',
                               null=False,
                               blank=False)

    class Meta:
        ordering = ['name']


    def __str__(self):
        if self.vat_id:
            return f'{self.name} - {self.vat_id} ({self.country})'
        else:
            return f'{self.name} ({self.country})'
