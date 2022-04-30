# crud_sales

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rodar o en_gen para gerar o arquivo .env
* Rode as migrações.
* Popule o banco de dados com dados ficticios

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
```