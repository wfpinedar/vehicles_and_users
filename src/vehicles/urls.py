from django.urls import path
from django.conf.urls import url

from .views import TradeMarkTemplateView
from .views import TradeMarkFormView
from .views import NewOwnerVehicleFormView
from .views import OwnerListView
from .views import OwnerDetailView
from .views import VehicleDetailView


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
         ),

    path(
        r'list_trademarks',
        TradeMarkTemplateView.as_view(),
        name="list_trademarks"
    ),

    path(
        r'trades_list',
        TradeMarkFormView.as_view(),
        name="trades_list"
    )
]
