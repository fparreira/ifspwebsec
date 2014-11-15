# coding: utf-8
from django.db import models

class Requerimento(models.Model):
    requerimento = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    permissao = models.CharField(max_length=100)

    def __unicode__(self):
        return self.requerimento