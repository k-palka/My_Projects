from django.urls import path
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('main/', MainView.as_view(), name='dashboard'),
    path('offer/<int:id>/', OfferDetailView.as_view(), name='offer-detail'),
    path('offer/list/', OfferListView.as_view(), name='offer-list'),
    path('offer/add/', OfferAddView.as_view(), name='add-offer'),
    path('procedure/list/', ProcedureListView.as_view(), name='procedure-list'),
    path('procedure/<int:id>/', ProcedureDetailView.as_view(), name='procedure-detail'),
    path('procedure/add/', ProcedureAddView.as_view(), name='add-procedure'),
    path('procedure/add-offer/', ProcedureAddOfferView.as_view(), name='add-offer-to-procedure'),
    path('evaluation/<int:pk>/', EvaluationDetailView.as_view(), name='evaluation'),
    path('evaluation/list/', EvaluationListView.as_view(), name='evaluation-list'),
    path('evaluation/create/', EvaluationAddView.as_view(), name='evaluation-create'),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),

]
