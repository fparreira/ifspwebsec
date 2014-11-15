# coding: utf-8
from django.test import TestCase
from websec.requerimentos.forms import RequerimentoForm
from websec.requerimentos.models import Requerimento

class RequerimentoTeste(TestCase):
    def setUp(self):
        self.resp = self.client.get('/requerimento/')

    def testeGet(self):
        self.assertEqual(200, self.resp.status_code)

    def testeTemplate(self):
        self.assertTemplateUsed(self.resp, 'requerimentos/requerimento_form.html')

    def testeHtml(self):
        #html deve conter inputs e form
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 3)
        self.assertContains(self.resp, 'type="text"', 1)
        self.assertContains(self.resp, '<select', 2)
        self.assertContains(self.resp, 'type="submit"')

    def testeCSRF(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def teste_existe_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, RequerimentoForm)

class RequerimentoPostTeste(TestCase):
    def setUp(self):
        data = dict(requerimento='Abono de Faltas', status='ativo', permissao='web')
        self.resp = self.client.post('/requerimento/', data)

    def testePost(self):
        self.assertEqual(302, self.resp.status_code)

    def testeSave(self):
        self.assertTrue(Requerimento.objects.exists())