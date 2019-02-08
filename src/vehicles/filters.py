from django_filters import FilterSet, ChoiceFilter, CharFilter
from .models import Owner, Vehicle
from .data import ORDER_CHOICES


class OwnerFilter(FilterSet):

    vehicle__id = CharFilter(field_name='vehicle__id', label='Plate', lookup_expr='icontains')
    ordering = ChoiceFilter(label='Ordering', choices=ORDER_CHOICES, method='filter_by_order')

    class Meta:
        model = Owner
        fields = {
            'id': ['icontains'],
            'name': ['icontains'],
            'last_name': ['icontains'],
        }




    def filter_by_order(self, queryset, name, value):
        expression = 'name' if value == 'ascending' else '-name'
        return queryset.order_by(expression)
