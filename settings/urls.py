from django.urls import path
from .views import GenderListView


urlpatterns = [
    path('genders/', GenderListView.as_view(), name='genders'),
]