from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from ..models import Tenant


class TenantListView(ListView):
    model = Tenant


class TenantCreateView(CreateView):
    model = Tenant
    fields = '__all__'
    success_url = reverse_lazy("settings:tenants")


class TenantUpdateView(UpdateView):
    model = Tenant
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy("settings:tenants")


class TenantDeleteView(DeleteView):
    model = Tenant
    fields = '__all__'
    success_url = reverse_lazy("settings:tenants")





'''
Za referncu:
    fields = [
        'name',
        'vat_id',
        'street_and_number',
        'postal_number',
        'city',
        'country'
    ]

'''