from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.views import View
import random

# Create your views here.


# def index(request):
#     return HttpResponse("Hello world. You are in the offer index")

class IndexView(View):

    def get(self, request):
        procedures = Procedure.objects.all()
        procedures_list = list(procedures)
        first_procedure = random.choice(procedures_list)
        second_procedure = random.choice(procedures_list)
        third_procedure = random.choice(procedures_list)
        return render(request, "index.html", context={'first_procedure': first_procedure, 'second_procedure': second_procedure,
                                                      'third_procedure': third_procedure})


