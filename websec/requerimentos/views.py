# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from websec.requerimentos.forms import RequerimentoForm
from websec.requerimentos.models import Requerimento
from django.shortcuts import get_object_or_404

def requerimento(request):
    if request.method == 'POST':
        return create(request)
    else:
        return novo(request)

def novo(request):
    return render(request, 'requerimentos/requerimento_form.html', {'form': RequerimentoForm()})

def create(request):
    form = RequerimentoForm(request.POST)
    form.full_clean()
    obj = Requerimento(**form.cleaned_data)
    obj.save()
    #obj = form.save()
    return HttpResponseRedirect('/requerimento/%d/' % obj.pk)

def detalhe(request, pk):
    requerimento = get_object_or_404(Requerimento, pk=pk)
    return render(request, 'requerimentos/requerimento_detalhe.html', {'requerimento':requerimento})
