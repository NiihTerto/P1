"""DONO: P1 - Grupo 1 (Fundação)
Usada por todas as regras (rules_*.py). A view mostra a mensagem ao usuário.
"""


class RegraNegocioError(Exception):
    """Violação de regra de negócio. Ex.: RegraNegocioError("RN06", "o veículo já possui reserva nesse período.")"""

    def __init__(self, codigo, mensagem):
        self.codigo = codigo
        self.mensagem = mensagem
        super().__init__(f"{codigo}: {mensagem}")
