from django.urls import path
from .views import (GenderListView,
                    TenantListView,
                    TenantCreateView,
                    TenantUpdateView,
                    TenantDeleteView)


urlpatterns = [
    path('genders/', GenderListView.as_view(), name='genders'),
    path('tenants/', TenantListView.as_view(), name='tenants'),
    path('tenants/add/', TenantCreateView.as_view(), name='tenant_add'),
    path('tenants/update/<int:pk>', TenantUpdateView.as_view(), name='tenant_update'),
    path('tenants/delete/<int:pk>', TenantDeleteView.as_view(), name='tenant_delete'),
]