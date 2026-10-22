"""DONO: P8 - Grupo 3 (Telas)
TODO: UC03 - busca de disponibilidade, nova reserva, confirmação com o código e
cancelamento. Capture RegraNegocioError e mostre a mensagem com django.contrib.messages.
"""
from django.contrib.auth.decorators import login_required  # noqa: F401
from django.shortcuts import render  # noqa: F401
