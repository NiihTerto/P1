"""DONO: P4 - Grupo 2 (Domínio)
TODO: criar as enumerações como django.db.models.TextChoices.
ENTREGAR NO PRIMEIRO DIA: P2 e P3 dependem deste arquivo.

  StatusVeiculo    DISPONIVEL, LOCADO, MANUTENCAO, INATIVO
  StatusReserva    ATIVA, CONVERTIDA, CANCELADA, EXPIRADA
  StatusLocacao    EM_ANDAMENTO, FINALIZADA, ATRASADA
  CategoriaCNH     A, B, C, D, E
  NivelCombustivel VAZIO(0), UM_QUARTO(1), METADE(2), TRES_QUARTOS(3), CHEIO(4)
                   -> precisa de um jeito de obter o valor em quartos
  PerfilUsuario    ATENDENTE, GERENTE
"""
from django.db import models  # noqa: F401
