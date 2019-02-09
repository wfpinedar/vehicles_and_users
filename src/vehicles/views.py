from django.db import transaction
from django.db.models import Count
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import FormView

from .data import TRADEMARK_CHOICES
from .forms import TradeMarkForm
from .forms import VehicleMemberFormSet
from .filters import OwnerFilter
from .models import Owner
from .models import Vehicle


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


class TradeMarkTemplateView(TemplateView):
    template_name = 'trademarks_report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        registers = Vehicle.objects.values('trademark').annotate(count=Count('trademark'))

        trademarks = dict(TRADEMARK_CHOICES)

        count_list = []
        for register in registers:
            count_list.append({
                'trademark': trademarks[register['trademark']],
                'count': register['count']
            })

        context['registers'] = count_list

        return context


class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicles.html'


class TradeMarkFormView(FormView):
    template_name = 'trades_list.html'
    form_class = TradeMarkForm

    def form_valid(self, form):
        data = form.cleaned_data
        trademarks = dict(TRADEMARK_CHOICES)
        trademark = int(data.get('trademark', 0))

        context = self.get_context_data()
        context.update({
            'vehicles': Vehicle.objects.filter(trademark=trademark),
            'trademark': trademarks.get(trademark)
        })


        return render(self.request, self.template_name, context)
