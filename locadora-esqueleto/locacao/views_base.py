"""DONO: P1 - Grupo 1 (Fundação)
TODO (todas com @login_required, exceto o login):
  painel(request)        RF15: livres, em andamento, atrasadas, manutenção, faturado hoje,
                         retiradas e devoluções do dia
  reserva_lista / reserva_detalhe      RF14 (filtro por status)
  locacao_lista / locacao_detalhe      RF14 (filtro por status)
O login e o logout usam as views prontas do Django (django.contrib.auth.views).
Chame operacoes.atualizar_status_temporais() no início das telas.
"""
from django.contrib.auth.decorators import login_required  # noqa: F401
from django.shortcuts import render  # noqa: F401
