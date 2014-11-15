# coding: utf-8
from django.test import TestCase
from websec.requerimentos.models import Requerimento

class RequerimentoTest(TestCase):
    def setUp(self):
        self.obj = Requerimento(
            requerimento='Abono de Faltas',
            status='ativo',
            permissao='web'
        )

    def test_create(self):
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_unicode(self):
        self.assertEqual(u'Abono de Faltas', unicode(self.obj))