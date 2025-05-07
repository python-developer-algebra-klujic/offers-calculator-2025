from django.views.generic import ListView

from ..models import Gender


class GenderListView(ListView):
    model = Gender
