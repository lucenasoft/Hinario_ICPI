from django.shortcuts import render

from hinario.models import Hino

# Create your views here.

def lista_hinos(request):
    hino = Hino.objects.all()
    return render(request,'hinario.html',context={
        'hinos':hino
    })