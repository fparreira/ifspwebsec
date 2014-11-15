# coding: utf-8
from django.test import TestCase
from websec.requerimentos.models import Requerimento

class DetalheTeste(TestCase):
    def setUp(self):
        r = Requerimento.objects.create(requerimento='Abono de faltas', status='ativo', permissao='web')
        self.resp = self.client.get('/requerimento/%d/' % r.pk)

    def teste_get(self):
        self.assertEqual(200, self.resp.status_code)

    def teste_template(self):
        self.assertTemplateUsed(self.resp, 'requerimentos/requerimento_detalhe.html')

    def teste_contexto(self):
        'o contexto deve ter uma instancia de requerimento'
        requerimento = self.resp.context['requerimento']
        self.assertIsInstance(requerimento, Requerimento)

    def teste_html(self):
        'testa se os dados do requerimento foram renderizados'
        self.assertContains(self.resp, 'Abono de faltas')

class DetalheNaoEncontrado(TestCase):
    def teste_nao_encontrado(self):
        response = self.client.get('/requerimento/0/')
        self.assertEqual(404, response.status_code)

