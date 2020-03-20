from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import random
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from .models import *
from .forms import *
from django.views import View
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
# from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


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
        latest_oferts_lists = Offert.objects.order_by('-submission')[:4]
        offer_counter = Offert.objects.count()
        procedure_counter = Procedure.objects.count()
        return render(request, "dashboard.html", {'procedure_counter': procedure_counter,
                                                  'offer_counter': offer_counter,
                                                  'last_added_procedure': last_added_procedure,
                                                  'latest_oferts_lists': latest_oferts_lists,
                                                  })


class OfferDetailView(DetailView):
    model = Offert
    context_object_name = 'oferta'
    template_name = 'offer_detail.html'


class OfferListView(View):

    def get(self, request):
        offerts_list = Offert.objects.order_by('submission')
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
        procedures_list = Procedure.objects.order_by('-publish')
        paginator = Paginator(procedures_list, 5)

        page = request.GET.get('page')
        procedures = paginator.get_page(page)

        context = {'procedures': procedures}
        return render(request, 'procedure_list.html', context)


class ProcedureDetailView(View):

    def get(self, request, id):
        procedure = Procedure.objects.get(id=id)
        offerts = Offert.objects.filter(procedure_id=id).order_by('price')
        offerts_list = list(offerts)
        employees = Role.objects.filter(procedure_id=id).distinct()
        empl_list = list(employees)
        return render(request, 'procedure_details.html',
                      context={'procedure': procedure, 'offerts': offerts,
                               'employees': employees, 'empl_list': empl_list,
                               'offerts_list': offerts_list})


class ProcedureAddView(View):
    def get(self, request):
        return render(request, "procedure_add.html")

    def post(self, request):
        numer = request.POST.get('procedure_numer')
        title = request.POST.get('procedure_title')
        publish = request.POST.get('procedure_publish')
        open = request.POST.get('procedure_open')
        close = request.POST.get('procedure_close')
        status = request.POST.get('procedure_status')

        if "" in (numer, title, publish, status):
            context = {'alert': 'Wypełnij poprawnie wszystkie pola!'}
            return render(request, 'procedure_add.html', context)

        Procedure.objects.create(numer=numer, title=title, publish=publish,
                                 open=open, close=close, status=status)
        return redirect(reverse('procedure-list'))


class ProcedureAddOfferView(View):

    def get(self, request):
        zamowienia = Procedure.objects.order_by('numer')
        oferty = Offert.objects.order_by('company_name')
        komisja = Employee.objects.order_by('last_name')
        funkcja = Role.objects.order_by('roles')
        context = {'zamowienia': zamowienia, 'oferty': oferty, 'komisja': komisja, 'funkcja': funkcja}
        return render(request, 'procedure_add_offer.html', context)


# class ProcedureAddView(CreateView):
#     model = Procedure
#     fields = ['numer', 'title', 'publish', 'slug'
#               'open', 'status']
#     template_name = 'procedure_add.html'
#     success_url = reverse_lazy('procedure-detail')
#
#     def get_success_url(self, **kwargs):
#         return reverse_lazy('status', kwargs={'status': self.object.status})

class TestView(View):
    pass
