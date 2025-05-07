from django.views.generic import ListView
from django.views.generic.edit import CreateView
from ..models import Tenant


class TenantListView(ListView):
    model = Tenant


class TenantCreateView(CreateView):
    model = Tenant
    fields = [
        'name',
        'vat_id',
        'street_and_number',
        'postal_number',
        'city',
        'country'
    ]
