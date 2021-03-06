from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'websec.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'websec.core.views.home', name='home'),
    url(r'^requerimento/$', 'websec.requerimentos.views.requerimento', name='requerimento'),
    url(r'^requerimento/(\d+)/$', 'websec.requerimentos.views.detalhe', name='detalhe'),
    url(r'^consulta/$', 'websec.requerimentos.views.consulta', name='consulta'),

    url(r'^admin/', include(admin.site.urls)),
)
