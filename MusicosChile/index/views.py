from django.shortcuts import render
from . models import Mensaje, Musico
from django.views import generic

# Create your views here.
def index(request)
    num_Mensaje = Mensaje.objects.all().count()
    num_Musico = Musico.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_mensaje': num_Mensaje, 'num_musico': num_Musico},
    )