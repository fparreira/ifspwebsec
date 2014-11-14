# coding: utf-8
from django.test import TestCase

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
        self.assertContains(self.resp, '<input', 2)
        self.assertContains(self.resp, 'type="text"', 1)
        self.assertContains(self.resp, '<select', 2)
        self.assertContains(self.resp, 'type="submit"')
