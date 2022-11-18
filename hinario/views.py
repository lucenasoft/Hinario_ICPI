from django.shortcuts import get_object_or_404, render

from hinario.models import Hino

# Create your views here.

def hinos01(request):
    hinos01 = Hino.objects.all()[:100]
    return render(request,'hinos01.html',context={
        'hinos01':hinos01,
    })

def hinos02(request):
    hinos02 = Hino.objects.all()[100:200]
    return render(request,'hinos02.html',context={
        'hinos02':hinos02,
    })

def hinos03(request):
    hinos03 = Hino.objects.all()[200:300]
    return render(request,'hinos03.html',context={
        'hinos03':hinos03,
    })

def hinos04(request):
    hinos04 = Hino.objects.all()[300:400]
    return render(request,'hinos04.html',context={
        'hinos04':hinos04,
    })

def hinos05(request):
    hinos05 = Hino.objects.all()[400:500]
    return render(request,'hinos05.html',context={
        'hinos05':hinos05,
    })

def hino(request,id):
    hino = get_object_or_404(Hino, pk=id)
    return render(request,'hino-view.html',context= {
        'hino': hino,
        'search': False,
    })