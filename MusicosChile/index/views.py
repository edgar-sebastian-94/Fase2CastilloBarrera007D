from django.shortcuts import render
from . models import Musico, Mensaje
from django.views import generic

# Create your views here.
def index(request):
    

    num_Musicos = Musico.objects.all().count()
    num_Mensajes = Mensaje.objects.all().count()


    return render(
        request,
        'index.html',
        context={'num_musicos': num_Musicos, 'num_mensajes': num_Mensajes, 
        },

        
    )

def perfil(request):
    

    num_Musicos = Musico.objects.all().count()
    num_Mensajes = Mensaje.objects.all().count()


    return render(
        request,
        'perfil.html',
        context={'num_musicos': num_Musicos, 'num_mensajes': num_Mensajes, 
        },

        
    )  

def buscar(request):
    

    num_Musicos = Musico.objects.all().count()
    num_Mensajes = Mensaje.objects.all().count()


    return render(
        request,
        'buscar.html',
        context={'num_musicos': num_Musicos, 'num_mensajes': num_Mensajes, 
        },

        
    )            

def registro(request):
    

    num_Musicos = Musico.objects.all().count()
    num_Mensajes = Mensaje.objects.all().count()


    return render(
        request,
        'registro.html',
        context={'num_musicos': num_Musicos, 'num_mensajes': num_Mensajes, 
        },

        
    )    



