"""DONO: P2 - Grupo 1 (Fundação)
TODO: validadores usados pelo modelo Veiculo.
  validar_placa(valor)    formato antigo (ABC-1234) ou Mercosul (ABC1D23)
  validar_chassi(valor)   17 caracteres, sem as letras I, O e Q
Ao falhar, levantam django.core.exceptions.ValidationError.
"""
from django.core.exceptions import ValidationError  # noqa: F401


def validar_placa(valor):
    raise NotImplementedError


def validar_chassi(valor):
    raise NotImplementedError
