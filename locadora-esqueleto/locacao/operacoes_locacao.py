"""DONO: P9 - Grupo 3 (Telas)
Casos de uso UC04 e UC05.

TODO:
  registrar_retirada(reserva, funcionario, km_saida, combustivel_saida, caucao)   (e a versão de balcão, sem reserva)
        RN13, RN14, RN15: reserva -> CONVERTIDA, veículo -> LOCADO, cria Locacao EM_ANDAMENTO
        SNAPSHOT DE PREÇO: copia valor_diaria e valor_caucao da categoria para a locação
  previa_devolucao(locacao, devolucao_real, km_retorno, combustivel_retorno)
        calcula o extrato SEM gravar (para mostrar antes de confirmar)
  registrar_devolucao(locacao, devolucao_real, km_retorno, combustivel_retorno, avaria="")
        RN16-RN19: grava valores, finaliza a locação, veículo -> DISPONIVEL
        (ou MANUTENCAO se houve avaria; nesse caso a caução é retida)
"""
from django.db import transaction  # noqa: F401

from . import rules, services  # noqa: F401


def registrar_retirada(reserva, funcionario, km_saida, combustivel_saida, caucao):
    raise NotImplementedError


def previa_devolucao(locacao, devolucao_real, km_retorno, combustivel_retorno):
    raise NotImplementedError


def registrar_devolucao(locacao, devolucao_real, km_retorno, combustivel_retorno, avaria=""):
    raise NotImplementedError
