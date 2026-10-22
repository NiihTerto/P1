"""DONO: P1 - Grupo 1 (Fundação)
Reúne as regras para o resto do código importar de um lugar só:
    from locacao import rules
Cada arquivo tem um dono: rules_reserva.py (P5) e rules_operacao.py (P6).
"""
from .rules_operacao import *  # noqa: F401,F403
from .rules_reserva import *  # noqa: F401,F403
