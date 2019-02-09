from django import forms

from .data import TRADEMARK_CHOICES
from .models import Vehicle
from .models import Owner


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ()


VehicleMemberFormSet = forms.inlineformset_factory(Owner, Vehicle, form=VehicleForm)


class TradeMarkForm(forms.Form):
    trademark = forms.ChoiceField(
        choices=((None, '--------'),) + TRADEMARK_CHOICES
    )