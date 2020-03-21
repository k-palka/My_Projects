from django.shortcuts import render, redirect
import random
from django.urls import reverse
from .forms import *
from django.views import View
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
        latest_oferts_lists = Offert.objects.order_by('-submission')[:4]
        offer_counter = Offert.objects.count()
        procedure_counter = Procedure.objects.count()
        return render(request, "dashboard.html", {'procedure_counter': procedure_counter,
                                                  'offer_counter': offer_counter,
                                                  'last_added_procedure': last_added_procedure,
                                                  'latest_oferts_lists': latest_oferts_lists,
                                                  })


class OfferDetailView(View):

    def get(self, request, id):
        oferta = Offert.objects.get(id=id)
        komisja = Role.objects.filter(procedure_id=oferta.procedure_id).distinct()
        komisja_list = list(komisja)
        komentarz = Evaluation.objects.filter(offert_id=oferta.id).distinct()
        komentarz_list = list(komentarz)
        context = {'oferta': oferta,
                   'komisja': komisja,
                   'komisja_list': komisja_list,
                   'komentarz': komentarz,
                   'komentarz_list': komentarz_list}
        return render(request, 'offer_detail.html', context)


class OfferListView(View):

    def get(self, request):
        offerts_list = Offert.objects.order_by('submission')
        paginator = Paginator(offerts_list, 10)

        page = request.GET.get('page')
        offerts = paginator.get_page(page)

        context = {'offerts': offerts}
        return render(request, 'offer_list.html', context)


class OfferAddView(CreateView):
    model = Offert
    fields = '__all__'


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


class EvaluationDetailView(DetailView):
    model = Evaluation
    template_name = 'evaluation_details.html'


class EvaluationListView(ListView):
    model = Evaluation
    template_name = 'evaluation_list.html'


class EvaluationAddView(CreateView):
    model = Evaluation
    fields = '__all__'

