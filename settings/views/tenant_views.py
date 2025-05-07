from django.views.generic import ListView
from ..models import Tenant


class TenantListView(ListView):
    model = Tenant
