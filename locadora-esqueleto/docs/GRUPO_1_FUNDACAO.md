# Grupo 1 - Fundação

Cada pessoa mexe **só nos próprios arquivos**. Se precisar de mudança em arquivo de outro, converse com o dono ou comente no Pull Request dele. Antes de abrir um PR: `python manage.py test` verde.

## P1

**Entrega:** Git e integração, login, layout base, painel do dia e listas de reservas/locações (RF01, RF14, RF15)

**Depende de:** ninguém na Fase 0. Painel e listas esperam os modelos de P2 e P3.

**Seus arquivos:**

- `locacao/admin.py`
- `locacao/apps.py`
- `locacao/excecoes.py`
- `locacao/forms.py`
- `locacao/models.py`
- `locacao/operacoes.py`
- `locacao/rules.py`
- `locacao/templates/locacao/base.html`
- `locacao/templates/locacao/locacao_detalhe.html`
- `locacao/templates/locacao/locacao_lista.html`
- `locacao/templates/locacao/painel.html`
- `locacao/templates/locacao/reserva_detalhe.html`
- `locacao/templates/locacao/reserva_lista.html`
- `locacao/templates/registration/login.html`
- `locacao/tests/test_painel.py`
- `locacao/urls.py`
- `locacao/validators.py`
- `locacao/views_base.py`

## P2

**Entrega:** Modelos Categoria, Veículo e Reserva; validadores de placa e chassi; admin; dados de exemplo da frota (RF03)

**Depende de:** enums.py do P4 (1º dia). Refere-se ao Cliente do P3 pelo nome, sem esperar.

**Seus arquivos:**

- `locacao/admin_frota.py`
- `locacao/dados_frota.py`
- `locacao/models_frota.py`
- `locacao/tests/test_validators_veiculo.py`
- `locacao/validators_veiculo.py`

## P3

**Entrega:** Modelos Cliente (com CNH), Funcionário e Locação; validador de CPF; RN19; admin; comando seed

**Depende de:** enums.py do P4.

**Seus arquivos:**

- `locacao/admin_clientes.py`
- `locacao/management/commands/seed.py`
- `locacao/models_clientes.py`
- `locacao/tests/test_cliente_locacao.py`
- `locacao/validators_cliente.py`

