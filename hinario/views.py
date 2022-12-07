from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from hinario.models import Hino

# Create your views here.

def hinos(request):
    hinos_list = Hino.objects.all()
    search = request.GET.get('search')
    paginator = Paginator(hinos_list, 100)
    page = request.GET.get('page')
    hinos = paginator.get_page(page)
    if search:
        hinos = hinos_list.filter(titulo__icontains=search)
    return render(request,'hinos01.html',context={
        'hinos01':hinos,
        'navbar_page': True
    })

def hino(request,id):
    hino = get_object_or_404(Hino, pk=id)
    return render(request,'hino-view.html',context= {
        'hino': hino,
        'search': False,
        'navbar_page': False
    })

def sobre(request):
    return render(request, 'sobre.html', context= {
        'search': False,
        'navbar_page': False,
    })