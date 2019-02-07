from django.shortcuts import render
from django.views.generic import CreateView
from .forms import VehicleMemberFormSet
from .models import Owner
from django.db import transaction
from django.urls import reverse_lazy

# Create your views here.
class NewOwnerVehicleFormView(CreateView):
    template_name = 'insert.html'
    model = Owner
    fields = ['id', 'name', 'last_name', 'id_image']
    success_url = "/owner"

    def get_context_data(self, **kwargs):
        data = super(NewOwnerVehicleFormView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['vehicles'] = VehicleMemberFormSet(self.request.POST)
        else:
            data['vehicles'] = VehicleMemberFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        vehicles = context['vehicles']
        with transaction.atomic():
            self.object = form.save()

            if vehicles.is_valid():
                vehicles.instance = self.object
                vehicles.save()
        return super(NewOwnerVehicleFormView, self).form_valid(form)
