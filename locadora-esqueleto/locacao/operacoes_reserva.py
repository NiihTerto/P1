"""DONO: P8 - Grupo 3 (Telas)
Casos de uso UC03: une modelos + regras + fórmulas, dentro de transações.

TODO:
  veiculos_disponiveis(retirada, devolucao, categoria=None)
        RN05: só status DISPONIVEL; RN07: fora MANUTENCAO e INATIVO;
        RN06: sem reserva ATIVA nem locação EM_ANDAMENTO sobrepostas (use rules.ha_sobreposicao)
  criar_reserva(cliente, veiculo, retirada, devolucao)
        @transaction.atomic + select_for_update no veículo; valida RN01-RN04, RN06, RN08-RN10;
        gera código único; calcula valor_estimado (services); cria a reserva ATIVA
  cancelar_reserva(reserva, agora)
        RN11: grátis até 24 h antes; depois, multa de 20%
  atualizar_status_temporais(agora=None)
        RN12: reservas ATIVAS vencidas -> EXPIRADA; RN17: locações vencidas -> ATRASADA
"""
from django.db import transaction  # noqa: F401

from . import rules, services  # noqa: F401


def veiculos_disponiveis(retirada, devolucao, categoria=None):
    raise NotImplementedError


def criar_reserva(cliente, veiculo, retirada, devolucao):
    raise NotImplementedError


def cancelar_reserva(reserva, agora=None):
    raise NotImplementedError


def atualizar_status_temporais(agora=None):
    raise NotImplementedError
