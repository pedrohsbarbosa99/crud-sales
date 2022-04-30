# crud_sales

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rodar o en_gen para gerar o arquivo .env
* Rode as migrações.

```
git clone ...
cd seletivo-backend-napp
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
```