"""DONO: P5 - Grupo 2 (Domínio)
TODO: para cada regra, um teste que passa e um que falha. Casos de borda: exatamente
21 anos, exatamente 24 h antes, exatamente 4 h depois.
"""
from django.test import SimpleTestCase

from locacao import rules  # noqa: F401


class RegrasReservaTests(SimpleTestCase):
    def test_rn01_idade_minima(self):
        self.skipTest("TODO P5")
