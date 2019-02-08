from django.urls import path
from django.conf.urls import url
from .views import NewOwnerVehicleFormView, OwnerListView, OwnerDetailView, VehicleDetailView

urlpatterns = [
    path(
        r'owner',
        NewOwnerVehicleFormView.as_view(),
        name="new_owner"
    ),
    path(
        r'',
        NewOwnerVehicleFormView.as_view(),
        name="new_owner"
    ),

    path(
        '<int:pk>/',
        OwnerDetailView.as_view(),
        name='detail'
    ),
    path(
        'vehicle/(?P<pk>[0-9]+)/\\$$',
        VehicleDetailView.as_view(),
        name='vehicle'
    ),
    path(r'list_owners',
         OwnerListView.as_view(),
         name="list_owners"
         )
]
