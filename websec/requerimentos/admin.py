# coding: utf-8
from django.contrib import admin
from websec.requerimentos.models import Requerimento

class RequerimentoAdmin(admin.ModelAdmin):
    list_display = ('requerimento', 'status', 'permissao')

admin.site.register(Requerimento, RequerimentoAdmin)