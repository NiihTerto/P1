"""DONO: P4 - Grupo 2 (Domínio)
TODO: um teste por fórmula + o exemplo numérico completo (R$ 690,00).
Use django.test.SimpleTestCase (sem banco). Cubra: frações de 24 h, tolerância
exata de 60 min, arredondamento HALF_UP, combustível sem crédito.
Rodar: python manage.py test locacao.tests.test_services
"""
from django.test import SimpleTestCase

from locacao import services  # noqa: F401


class FormulasTests(SimpleTestCase):
    def test_exemplo_numerico_690(self):
        self.skipTest("TODO P4")
