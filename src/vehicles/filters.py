from django_filters import FilterSet, ChoiceFilter
from .models import Owner
from .data import ORDER_CHOICES


class OwnerFilter(FilterSet):

    ordering = ChoiceFilter(label='Ordering', choices=ORDER_CHOICES, method='filter_by_order')


    class Meta:
        model = Owner
        fields = {
            'id': ['icontains'],
            'name': ['icontains'],
            'last_name': ['icontains']
        }

    def filter_by_order(self, queryset, name, value):
        expression = 'name' if value == 'ascending' else '-name'
        return queryset.order_by(expression)
