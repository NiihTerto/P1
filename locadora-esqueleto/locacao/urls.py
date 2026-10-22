"""DONO: P1 - Grupo 1 (Fundação)
Junta as rotas de todos. Cada grupo de telas edita só o seu urls_*.py.
Em config/urls.py (P1): path("", include("locacao.urls"))
"""
from django.urls import include, path  # noqa: F401

from . import views_base  # noqa: F401

urlpatterns = [
    # TODO P1: path("", views_base.painel, name="painel"),
    path("", include("locacao.urls_cadastro")),
    path("", include("locacao.urls_reserva")),
    path("", include("locacao.urls_locacao")),
]
