from django.shortcuts import get_object_or_404, render

from hinario.models import Hino

# Create your views here.

def hinos01(request):
    hinos01 = Hino.objects.all()
    search = request.GET.get('search')
    if search:
        hinos01 = hinos01.filter(titulo__icontains=search)
    return render(request,'hinos01.html',context={
        'hinos01':hinos01,
        'select_page': 1,
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