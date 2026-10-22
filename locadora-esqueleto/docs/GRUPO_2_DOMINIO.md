# Grupo 2 - Domínio

Cada pessoa mexe **só nos próprios arquivos**. Se precisar de mudança em arquivo de outro, converse com o dono ou comente no Pull Request dele. Antes de abrir um PR: `python manage.py test` verde.

## P4

**Entrega:** Enumerações (entregar no 1º dia) e fórmulas de cálculo (services.py)

**Depende de:** ninguém. Melhor ponto de partida.

**Seus arquivos:**

- `locacao/enums.py`
- `locacao/services.py`
- `locacao/tests/test_services.py`

## P5

**Entrega:** Regras de cliente, período, cancelamento e expiração: RN01 a RN04, RN08 a RN12

**Depende de:** excecoes.py do P1 (já incluído neste esqueleto).

**Seus arquivos:**

- `locacao/rules_reserva.py`
- `locacao/tests/test_rules_reserva.py`

## P6

**Entrega:** Sobreposição RN06, retirada e devolução (RN13, RN14, RN16) e teste ponta a ponta

**Depende de:** excecoes.py do P1 (já incluído). O teste ponta a ponta espera P7, P8 e P9.

**Seus arquivos:**

- `locacao/rules_operacao.py`
- `locacao/tests/test_ciclo_completo.py`
- `locacao/tests/test_rules_operacao.py`

