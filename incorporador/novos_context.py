from .models import Incorporador

def incorporador_recentes(request):
    lista_recentes = Incorporador.objects.all().order_by('-data_criacao')
    if lista_recentes:
        incorporador_destaque = lista_recentes[0]
    else:
        incorporador_destaque = None
    return {"incorporador_recentes":lista_recentes, "incorporador_destaque":incorporador_destaque}

def incorporador_popular(request):
    lista_popular = Incorporador.objects.all().order_by('-visualizacoes')
    return {"incorporador_popular":lista_popular}

