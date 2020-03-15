from django.shortcuts import render
from .models import *
from django.views import View
import random
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, DeleteView


# Create your views here.


class IndexView(View):

    def get(self, request):
        procedures = Procedure.objects.all()
        procedures_list = list(procedures)
        first_procedure = random.choice(procedures_list)
        second_procedure = random.choice(procedures_list)
        third_procedure = random.choice(procedures_list)
        return render(request, "index.html",
                      context={'first_procedure': first_procedure, 'second_procedure': second_procedure,
                               'third_procedure': third_procedure})


class MainView(View):

    def get(self, request):
        last_added_procedure = Procedure.objects.order_by('-publish').first()
        offer_counter = Offert.objects.count()
        procedure_counter = Procedure.objects.count()
        return render(request, "dashboard.html", {'procedure_counter': procedure_counter,
                                                  'offer_counter': offer_counter,
                                                  'last_added_procedure': last_added_procedure,
                                                  })


class OfferDetailView(View):

    def get(self, request, id):
        offerts = Offert.objects.filter(id=id)
        return render(request, 'offer_detail.html', context={'offerts': offerts})


class OfferListView(View):

    def get(self, request):
        offerts_list = Offert.objects.order_by('procedure')
        paginator = Paginator(offerts_list, 10)

        page = request.GET.get('page')
        offerts = paginator.get_page(page)

        context = {'offerts': offerts}
        return render(request, 'offer_list.html', context)


class OfferAddView(View):
    pass


class OfferModifyView(View):
    pass


class ProcedureListView(View):

    def get(self, request):
        procedures_list = Procedure.objects.order_by('-numer')
        paginator = Paginator(procedures_list, 3)

        page = request.GET.get('page')
        procedures = paginator.get_page(page)

        context = {'procedures': procedures}
        return render(request, 'procedure_list.html', context)


# class ProcedureDetailView(DetailView):
#     model = Procedure
#     template_name = 'procedure_details.html'

class ProcedureDetailView(View):

    def get(self, request, id):
        procedure = Procedure.objects.get(id=id)
        offerts = Offert.objects.filter(procedure_id=id).order_by('price')
        employees = Role.objects.filter(employee_id=id).distinct()
        return render(request, 'procedure_details.html',
                      context={'procedure': procedure, 'offerts': offerts, 'employees': employees})


class ProcedureAddView(View):
    pass


class ProcedureAddOfferView(View):
    pass
