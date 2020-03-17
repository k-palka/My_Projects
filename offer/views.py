from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import random
from django.urls import reverse_lazy
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


class ProcedureAddView(CreateView):
    pass
    """ widok dodawania Postępowania i przypisania pracowników"""


class ProcedureAddOfferView(View):

    def get(self, request):
        zamowienia = Procedure.objects.order_by('numer')
        oferty = Offert.objects.order_by('company_name')
        komisja = Employee.objects.order_by('last_name')
        funkcja = Role.objects.order_by('roles')
        context = {'zamowienia': zamowienia, 'oferty': oferty, 'komisja': komisja, 'funkcja': funkcja}
        return render(request, 'procedure_add_offer.html', context)

    # def post(self, request):
    #     zamowienie_id = request.POST.get('procedure_id')
    #     zamowienie = Procedure.objects.get(id=zamowienie_id)




#     def post(self, request):
#         plan_id = request.POST.get('plan_id')
#         plan = Plan.objects.get(id=plan_id)
#         recipe_name = request.POST.get('recipe_name')
#         recipe = Recipe.objects.get(name=recipe_name)
#         meal_name = request.POST.get('meal_name')
#         day_name = request.POST.get('day_name')
#         day = DayName.objects.get(name=day_name)
#         meal_number = request.POST.get('meal_number')
#
#         RecipePlan.objects.create(plan=plan, recipe=recipe, meal_name=meal_name, order=meal_number, day_name=day)
#
#         return redirect(reverse('plan-detail', kwargs={'id': plan_id}))


# class TestView(ListView):
#     model = Role
#     template_name = "test.html"

class TestView(View):

    def get(self, request):
        zamowienie = Procedure.objects.all()
        funkcje = Role.objects.all()
        zamowienie_counter = Procedure.objects.count()
        funkcje_counter = Role.objects.count()
        return render(request, "test.html", {'funkcje_counter': funkcje_counter,
                                            'zamowienie_counter': zamowienie_counter,
                                                  'zamowienie': zamowienie,
                                                  'funkcje': funkcje,})
