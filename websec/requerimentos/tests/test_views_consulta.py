# coding: utf-8
from django.test import TestCase
from websec.requerimentos.models import Requerimento

class ConsultaTeste(TestCase):
    def setUp(self):
        self.resp = self.client.get('/consulta/')

    def testeGet(self):
        self.assertEqual(200, self.resp.status_code)

    def teste_template(self):
        self.assertTemplateUsed(self.resp, 'requerimentos/requerimento_consulta.html')

    def teste_contexto(self):
        'teste se existe uma instancia de requerimentos no contexto'
        requerimento = self.resp.context['requerimento']
        self.assertIsInstance(requerimento, Requerimento)