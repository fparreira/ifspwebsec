# coding: utf-8
from django.test import TestCase
from websec.requerimentos.forms import RequerimentoForm

class RequerimentoFormTeste(TestCase):
    def teste_form_tem_campos(self):
        form = RequerimentoForm()
        self.assertItemsEqual(['requerimento', 'status', 'permissao'], form.fields)