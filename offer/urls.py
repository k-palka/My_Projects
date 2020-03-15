from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('main/', MainView.as_view(), name='dashboard'),
    path('offer/<int:pk>/', OfferDetailView.as_view(), name='offer-detail'),
    path('offer/list/', OfferListView.as_view(), name='offer-list'),
    path('offer/add/', OfferAddView.as_view(), name='add-offer'),
    path('offer/modify/<int:id>/', OfferModifyView.as_view(), name='modify-offer'),
    path('procedure/list/', ProcedureListView.as_view(), name='procedure-list'),
    path('procedure/<int:id>/', ProcedureDetailView.as_view(), name='procedure-detail'),
    path('procedure/add/', ProcedureAddView.as_view(), name='add-procedure'),
    path('procedure/add-offer/', ProcedureAddOfferView.as_view(), name='add-offer-to-procedure'),

]
