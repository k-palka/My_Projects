from .models import Procedure


def all_procedures(request):
    ctx = {'all_procedures': Procedure.objects.all()}
    return ctx
