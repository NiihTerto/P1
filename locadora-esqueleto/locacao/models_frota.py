"""DONO: P2 - Grupo 1 (Fundação)
TODO: modelos Categoria, Veiculo e Reserva.
Toda ForeignKey: related_name e on_delete=models.PROTECT.
Dinheiro: DecimalField(max_digits=10, decimal_places=2).

  Categoria  nome, valor_diaria, valor_caucao, valor_tanque_cheio, descricao
  Veiculo    placa (unique), chassi (unique), marca, modelo, ano_fabricacao, cor,
             km_atual, status (StatusVeiculo), categoria (FK)
  Reserva    codigo (unique), cliente (FK "locacao.Cliente" - texto, pois o modelo é do P3),
             veiculo (FK), retirada_prevista, devolucao_prevista,
             valor_estimado, status (StatusReserva)
"""
from django.db import models  # noqa: F401

from .enums import *  # noqa: F401,F403  (feito pelo P4)
