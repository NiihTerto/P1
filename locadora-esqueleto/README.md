# Esqueleto da pasta `locacao/` - Sistema de Locadora de Veículos

Este pacote contém **só o app `locacao/`** (arquivos vazios com instruções), separado por dono.
Os arquivos `config/`, `manage.py`, `venv/` e `.gitignore` vêm do `django-admin startproject` que o P1 já faz.

## Como colocar no seu projeto (P1)

1. Com o projeto Django já criado (`django-admin startproject config .`), **apague** a pasta `locacao/`
   criada pelo `startapp` e copie para o lugar dela a pasta `locacao/` deste pacote.
   Copie também a pasta `docs/`.
2. Em `config/settings.py`, em `INSTALLED_APPS`, deve constar `"locacao"`. Acrescente também:
   `LOGIN_URL = "login"`, `LOGIN_REDIRECT_URL = "painel"`, `LANGUAGE_CODE = "pt-br"`, `TIME_ZONE = "America/Sao_Paulo"`.
3. Em `config/urls.py`, inclua `path("", include("locacao.urls"))` e as rotas de login/logout
   (`django.contrib.auth.urls`).
4. Rode `python manage.py check` (o `NotImplementedError` só aparece quando uma função é chamada).
5. `git add .`, `git commit -m "chore: esqueleto por grupo"`, `git push` na branch `develop`.

## Como ler

- `docs/GRUPO_1_FUNDACAO.md`, `GRUPO_2_DOMINIO.md`, `GRUPO_3_TELAS.md`: o que cada pessoa faz e quais arquivos são seus.
- `docs/MAPA_DE_ARQUIVOS.md`: todos os arquivos e seus donos.
- Cada arquivo começa com `DONO: ...` e uma lista `TODO` do que implementar.

## Por que há tantos arquivos pequenos?

Para duas pessoas nunca editarem o mesmo arquivo (isso gera conflitos no Git). Os arquivos
`models.py`, `rules.py`, `operacoes.py`, `forms.py`, `admin.py` e `validators.py` só juntam os arquivos de cada dono.
