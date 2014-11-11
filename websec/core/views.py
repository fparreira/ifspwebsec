# coding: utf-8
#from django.http import HttpResponse
#from django.template import loader, Context
#from django.shortcuts import render_to_response
#from django.conf import settings
#from django.template import RequestContext
from django.shortcuts import render

def home(request):
    #return HttpResponse("Sistema Web Secretaria")

    #t = loader.get_template("index.html")
    #c = Context()
    #conteudo = t.render(c)
    #return HttpResponse(conteudo)

    #refatoracao
    #return render_to_response("index.html")

    #contexto = {'STATIC_URL': settings.STATIC_URL}
    #return render_to_response("index.html", contexto)

    #dry
    #contexto = RequestContext(request)
    #return render_to_response("index.html", contexto)

    #dry++
    return render(request, 'index.html')