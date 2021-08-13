from django.shortcuts import render, redirect
from .models import Hodimlar
from django.views.generic import DetailView, CreateView


def Index(request):
    return render(request, 'index.html')


def About(request):
    hodim = Hodimlar.objects.all()

    return render(request, 'about.html', {'hodimlar': hodim})


def Service(request):
    return render(request, 'service.html')


def HodimDetail(request, id):
    hodim = Hodimlar.objects.get(id=id)
    hodimlar = Hodimlar.objects.all()

    return render(request, 'hodim-detail.html', {
                                            'hodim': hodim,
                                            'hodimlar':hodimlar,
                                                 })

def Hodim(request):
    ishchi = Hodimlar.objects.all()

    return render(request, 'hodimlar.html', {
                                            'ishchi':ishchi
                           })

def IshchiDetail(request, id):
    hh = Hodimlar.objects.get(id=id)
    ischilar = Hodimlar.objects.all()
    return render(request, 'ishchi.html', {'hodim':hh, 'hodimlar':ischilar})


def HodimAdd(request):
    fio = request.POST['fio']
    phone = request.POST['phone']
    mut = request.POST['mut']
    add = request.POST['add']

    a = 5

    Hodimlar.objects.create(fio=fio, phone=phone, mutaxasislik=mut, address=add)

    return redirect('/about/')