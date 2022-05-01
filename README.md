# crud_sales

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rodar o en_gen para gerar o arquivo .env
* Rode as migrações.
* Popule o banco de dados com dados ficticios
* Rode os testes
* execute a aplicação

```
git clone git@github.com:pedrohsbarbosa99/crud-sales.git
cd crud-sales
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py populate_db
python manage.py createsuperuser --username="admin" --email=""
pytest
python manage.py runserver
```

## Na pagina inicial há um grafico com vendas por estado.
<a href="http://127.0.0.1:8000"></a>

### Siga para doc interativa

<a href="http://127.0.0.1:8000/api/docs" target="_blank">http://127.0.0.1:8000/api/docs</a>