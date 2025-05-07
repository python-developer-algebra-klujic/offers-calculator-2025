from django.urls import path
from .views import GenderListView, TenantListView, TenantCreateView


urlpatterns = [
    path('genders/', GenderListView.as_view(), name='genders'),
    path('tenants/', TenantListView.as_view(), name='tenants'),
    path('tenants/add/', TenantCreateView.as_view(), name='tenant_add'),
]