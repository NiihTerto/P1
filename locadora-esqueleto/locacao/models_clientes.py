"""DONO: P3 - Grupo 1 (Fundação)
TODO: modelos Cliente, Funcionario e Locacao.

  Cliente      nome, cpf (unique, validar_cpf), email, telefone, data_nascimento, endereco,
               ativo, e a CNH embutida: cnh_numero, cnh_categoria (CategoriaCNH), cnh_validade
  Funcionario  user (OneToOne com django.contrib.auth User), nome, matricula, perfil (PerfilUsuario)
  Locacao      reserva (OneToOne, null=True), cliente, veiculo, atendente (FK Funcionario),
               data_retirada, devolucao_prevista, devolucao_real (null),
               km_saida, km_retorno (null), combustivel_saida, combustivel_retorno (null),
               valor_diaria_aplicado, valor_caucao, valor_multa, valor_total, avaria, status

  RN19: Locacao.save() NÃO pode alterar uma locação FINALIZADA (levantar RegraNegocioError).
"""
from django.db import models  # noqa: F401

from .enums import *  # noqa: F401,F403  (feito pelo P4)
