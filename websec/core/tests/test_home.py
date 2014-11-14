# coding: utf-8
from django.test import TestCase

class HomeTeste(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def testeGet(self):
        #deve retornar status code 200
        self.assertEqual(200, self.resp.status_code)

    def testeTemplate(self):
        #deve usar o template index.html
        self.assertTemplateUsed(self.resp, 'index.html')


