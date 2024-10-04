# Stadtklima Orchestration

## Installation

Install docker and docker compose. Then in root folder, run

```sh
docker compose up
```

### REST API

#### Packages

REST API relies on

- [Flask-SQLAlchemy](https://github.com/pallets-eco/flask-sqlalchemy)
- [Flask-Migrate](https://github.com/miguelgrinberg/Flask-Migrate)
- [Flask-Admin[sqlalchemy]](https://github.com/pallets-eco/flask-admin)
- [connexion[swagger-ui,uvicorn]](https://github.com/spec-first/connexion)

```sh
# get a shell into the api container
docker compose exec api bash

# install pip packages

pip install -r requirements.txt
```

### PostgreSQL Database

Perform a database migration with

```sh
flask db check
```

If you change the models in `models.py`, create a new migration file with

```sh
flask db migrate -m "CHANGE MESSAGE"
```

## Run it
