from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from ..models import Gender


class GenderListView(ListView):
    model = Gender


class GenderCreateView(CreateView):
    model = Gender
    fields = '__all__'
    success_url = reverse_lazy("settings:genders")


class GenderUpdateView(UpdateView):
    model = Gender
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy("settings:genders")


class GenderDeleteView(DeleteView):
    model = Gender
    fields = '__all__'
    success_url = reverse_lazy("settings:genders")
