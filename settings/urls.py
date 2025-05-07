from django.urls import path
from .views import GenderListView, TenantListView


urlpatterns = [
    path('genders/', GenderListView.as_view(), name='genders'),
    path('tenants/', TenantListView.as_view(), name='tenants'),
]