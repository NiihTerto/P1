"""DONO: P6 - Grupo 2 (Domínio)
Sobreposição de períodos e regras de retirada/devolução. Funções PURAS.

TODO (teste primeiro, em tests/test_rules_operacao.py):

  ha_sobreposicao(nova_retirada, nova_devolucao, periodos)   RN06 (a regra mais importante)
        periodos = lista de (retirada, devolucao) já existentes
        Há conflito quando: nova_retirada < devolucao_existente
                        E:  nova_devolucao > retirada_existente
        Períodos que só se encostam NÃO conflitam.
        Os 8 cenários de teste: sobreposição total, período contido, parcial no
        início, parcial no fim, encaixe exato antes, encaixe exato depois,
        sem conflito, lista vazia.
  validar_reserva_convertivel(status_reserva)                RN13  só reserva ATIVA vira locação
  validar_dados_saida(km_saida, nivel_combustivel, km_atual_veiculo)   RN14  km e combustível obrigatórios; km >= km do veículo
  validar_km_retorno(km_saida, km_retorno)                   RN16  km de retorno >= km de saída
"""
from .excecoes import RegraNegocioError  # noqa: F401


def ha_sobreposicao(nova_retirada, nova_devolucao, periodos):
    raise NotImplementedError


def validar_reserva_convertivel(status_reserva):
    raise NotImplementedError


def validar_dados_saida(km_saida, nivel_combustivel, km_atual_veiculo):
    raise NotImplementedError


def validar_km_retorno(km_saida, km_retorno):
    raise NotImplementedError
