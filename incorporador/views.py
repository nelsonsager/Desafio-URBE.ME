from django.shortcuts import render, redirect, reverse
from .models import Incorporador, Usuario
from .forms import CriarContaForm
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin # passo isso quando quero bloquear views
                                                          # o LoginRequiredMixin vem antes da classe do objeto
                                                          # class ... (LoginRequiredMixin, TemplateView):

# Create your views here.

class Homepage(TemplateView):
    template_name = "homepage.html"

class Homeincorporador(ListView):
    template_name = "homeincorporador.html"
    model = Incorporador #object list do modelo

class Detalhesincorporador(DetailView):
    template_name = "detalhesincorporador.html"
    model = Incorporador #object -> 1 item do modelo

    def get(self, request, *args, **kwargs): #contabilizando vizualizacoes
        incorporador = self.get_object()
        incorporador.visualizacoes += 1
        incorporador.save()
        usuario = request.user
        usuario.incorporadoras_vistas.add(incorporador) #metodos que relacionam com o banco de dados (add e nao append)
        return super().get(request, *args,**kwargs) #redireciona o usuario para a url final

    def get_context_data(self, **kwargs):
        context = super(Detalhesincorporador,self).get_context_data(**kwargs)
        #filtrando tabela de incorporador para a mesma categoria
        incorporador_relacionado = Incorporador.objects.filter(categoria=self.get_object().categoria)
        context["incorporador_relacionado"] = incorporador_relacionado
        return context
    

class Pesquisaincorporador(ListView):
    template_name = "pesquisa.html"
    model = Incorporador 

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = Incorporador.objects.filter(descricao__icontains=termo_pesquisa)
            return object_list
        else:
            return None


class Paginaperfil(LoginRequiredMixin,UpdateView):
    template_name = "editarperfil.html"
    model = Usuario 
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse ('incorporador:homepage')

class Criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse ('incorporador:login')
