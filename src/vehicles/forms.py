from django import forms
from .models import Vehicle
from .models import Owner

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ()

VehicleMemberFormSet = forms.inlineformset_factory(Owner, Vehicle, form=VehicleForm)
