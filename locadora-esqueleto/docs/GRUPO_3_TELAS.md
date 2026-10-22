# Grupo 3 - Telas

Cada pessoa mexe **só nos próprios arquivos**. Se precisar de mudança em arquivo de outro, converse com o dono ou comente no Pull Request dele. Antes de abrir um PR: `python manage.py test` verde.

## P7

**Entrega:** UC01 Manter veículo e UC02 Manter cliente, com histórico (RF02, RF04, RF16)

**Depende de:** modelos de P2 e P3; pode começar pelo HTML.

**Seus arquivos:**

- `locacao/forms_cadastro.py`
- `locacao/templates/locacao/cliente_detalhe.html`
- `locacao/templates/locacao/cliente_form.html`
- `locacao/templates/locacao/cliente_lista.html`
- `locacao/templates/locacao/veiculo_form.html`
- `locacao/templates/locacao/veiculo_lista.html`
- `locacao/tests/test_views_cadastro.py`
- `locacao/urls_cadastro.py`
- `locacao/views_cadastro.py`

## P8

**Entrega:** UC03 Disponibilidade, reserva, cancelamento e expiração (RF05 a RF08, RF13)

**Depende de:** P2 e P3 (modelos), P4 (valor estimado), P5 e P6 (regras). Apoio: P5.

**Seus arquivos:**

- `locacao/forms_reserva.py`
- `locacao/operacoes_reserva.py`
- `locacao/templates/locacao/disponibilidade.html`
- `locacao/templates/locacao/reserva_confirmacao.html`
- `locacao/templates/locacao/reserva_nova.html`
- `locacao/tests/test_views_reserva.py`
- `locacao/urls_reserva.py`
- `locacao/views_reserva.py`

## P9

**Entrega:** UC04 Retirada e UC05 Devolução com extrato (RF09 a RF12)

**Depende de:** P8 (reservas), P4 (fórmulas), P6 (regras), P3 (Locacao). Apoio: P4.

**Seus arquivos:**

- `locacao/forms_locacao.py`
- `locacao/operacoes_locacao.py`
- `locacao/templates/locacao/devolucao_form.html`
- `locacao/templates/locacao/retirada_form.html`
- `locacao/tests/test_views_locacao.py`
- `locacao/urls_locacao.py`
- `locacao/views_locacao.py`

