"""DONO: P5 - Grupo 2 (Domínio)
Regras de cliente, período e reserva. Funções PURAS: recebem números, datas e
textos simples (nunca objetos do banco). Ao violar, levantam
RegraNegocioError("RNxx", "mensagem").

TODO (teste primeiro, em tests/test_rules_reserva.py):

  validar_idade(data_nascimento, data_retirada)            RN01  mínimo 21 anos na retirada
  validar_cnh(categoria, validade, devolucao_prevista)     RN02  categoria B ou superior e válida até a devolução
  validar_cliente_ativo(ativo)                             RN03  cliente inativo não reserva
  validar_sem_atraso(tem_locacao_atrasada)                 RN04  cliente com locação ATRASADA não reserva
  validar_periodo(retirada, devolucao, agora)              RN08  mínimo 1 diária, máximo 30 dias
                                                           RN09  retirada não pode ser no passado
                                                           RN10  devolução depois da retirada
  cancelamento_com_multa(retirada_prevista, agora)         RN11  True se faltar menos de 24 h
  reserva_expirada(retirada_prevista, agora)               RN12  True se passou mais de 4 h da hora prevista
"""
from .excecoes import RegraNegocioError  # noqa: F401


def validar_idade(data_nascimento, data_retirada):
    raise NotImplementedError


def validar_cnh(categoria, validade, devolucao_prevista):
    raise NotImplementedError


def validar_cliente_ativo(ativo):
    raise NotImplementedError


def validar_sem_atraso(tem_locacao_atrasada):
    raise NotImplementedError


def validar_periodo(retirada, devolucao, agora):
    raise NotImplementedError


def cancelamento_com_multa(retirada_prevista, agora):
    raise NotImplementedError


def reserva_expirada(retirada_prevista, agora):
    raise NotImplementedError
