from django.urls import path
from .views import NewOwnerVehicleFormView

urlpatterns = [
    path(
        r'owner',
        NewOwnerVehicleFormView.as_view(),
        name="new_owner"
    )
]
