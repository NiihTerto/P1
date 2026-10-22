"""DONO: P3 - Grupo 1 (Fundação)
Comando: python manage.py seed
TODO: chamar dados_frota.criar_categorias() e criar_veiculos() (P2), e criar
clientes e funcionários de exemplo (P3). Depois, reservas e locações de
exemplo (inclusive a locação nº 1 do exemplo de R$ 690,00) - todos, na Fase 3.
"""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Carrega dados de exemplo."

    def handle(self, *args, **options):
        raise NotImplementedError
