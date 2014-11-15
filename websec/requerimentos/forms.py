# coding: utf-8
from django import forms
from websec.requerimentos.models import Requerimento

class RequerimentoForm(forms.Form):
    optionsStatus = (('ativo','Ativo'),('inativo','Inativo'),)
    optionsPermissao = (('web','Web'), ('secretaria','Secretaria'),('professores','Professores'),('todos','Todos'),)

    requerimento = forms.CharField()
    status = forms.ChoiceField(choices=optionsStatus)
    permissao = forms.ChoiceField(choices=optionsPermissao)

#class RequerimentoForm(forms.ModelForm):
#   class Meta:
#        model = Requerimento