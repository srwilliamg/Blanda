from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import *
from .models import *

def fname(sintoma):
    a = []
    sintomas = caracteristica.objects.all()
    p0 = sintomas.filter(feature = sintoma)
    if len(p0) >=1:
        for j in p0[0].objetocaracteristica_set.all():
            a.append(j.obj.name)
    return a


def buscar(request):
    form = formBuscar(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            c1 = form.cleaned_data.get('c1')
            c2 = form.cleaned_data.get('c2')
            c3 = form.cleaned_data.get('c3')
            c4 = form.cleaned_data.get('c4')

            a = fname(c1)
            b = fname(c2)
            c = fname(c3)
            d = fname(c4)

            intersection1 = list(set(a) & set(b))
            intersection2 = list(set(a) & set(b))
            intersection3 = list(set(intersection1) & set(intersection2))

            return HttpResponse(intersection3[0])
    return render(request,'sistemaExperto/index.html',{'form':form})