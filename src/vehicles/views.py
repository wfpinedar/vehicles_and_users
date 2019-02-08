from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from .forms import VehicleMemberFormSet
from .models import Owner, Vehicle
from django.db import transaction
from .filters import OwnerFilter

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


class OwnerListView(ListView):
    model = Owner
    template_name = 'base_generic.html'


    def get_context_data(self, **kwargs):
        context = super(OwnerListView, self).get_context_data(**kwargs)
        context['filter'] = OwnerFilter(self.request.GET, queryset=self.get_queryset().values())
        return context


class OwnerDetailView(DetailView):
    model = Owner
    template_name = 'owners.html'


class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicles.html'