# coding: utf-8
from django.db import models

class Requerimento(models.Model):
    requerimento = models.CharField(max_length=100, verbose_name="Requerimento")
    status = models.CharField(max_length=10, verbose_name="Status")
    permissao = models.CharField(max_length=100, verbose_name="Permissão")

    def __unicode__(self):
        return self.requerimento