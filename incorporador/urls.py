from django.urls import path, reverse_lazy
from .views import Homepage, Homeincorporador, Detalhesincorporador, Pesquisaincorporador, Paginaperfil, Criarconta
from django.contrib.auth import views as auth_view #view padrao do django para login/logout, muda o nome para nao confundir

app_name = 'incorporador'

urlpatterns = [
    path("", Homepage.as_view(), name="homepage"),
    path("incorporadora/", Homeincorporador.as_view(), name="homeincorporador"),
    path("incorporadora/<int:pk>", Detalhesincorporador.as_view(), name="detalhesincorporador"),
    path("pesquisa/", Pesquisaincorporador.as_view(), name="pesquisa"),
    path("login/", auth_view.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_view.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("editarperfil/<int:pk>", Paginaperfil.as_view(), name="editarperfil"),
    path("criarconta/", Criarconta.as_view(), name="criarconta"),
    path("mudarsenha/", auth_view.PasswordChangeView.as_view(template_name="editarperfil.html", success_url=reverse_lazy("incorporador:homepage")), name="mudarsenha"),
] 
