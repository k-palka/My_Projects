from .models import Offert


def all_offerts(request):
    ctx = {'all_offerts': Offert.objects.all()}
    return ctx
