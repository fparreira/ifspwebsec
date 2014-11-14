# coding: utf-8
from django.shortcuts import render

def requerimento(request):
    return render(request, 'requerimentos/requerimento_form.html')
