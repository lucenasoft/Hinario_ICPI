from django.shortcuts import get_object_or_404, render

from hinario.models import Hino

# Create your views here.

def lista_hinos(request):
    hino = Hino.objects.all()
    return render(request,'home.html',context={
        'hinos':hino,
    })

def hino(request,id):
    hino = get_object_or_404(Hino, pk=id)
    return render(request,'hino-view.html',context= {
        'hino': hino,
        'search': False,
    })