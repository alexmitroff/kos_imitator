# KOS imitator based on django

## Add production settings
kos_imitator/settings/**prod.py**
```python
from kos_imitator.settings.base import *

SECRET_KEY = '52h#0@ivjh-jl+*)6^z2r6kfym9eqp-z&&ivwwslm@=mou6#sm'
DEBUG = False

ALLOWED_HOSTS = ['192.168.90.65']

STATIC_ROOT = "/var/www/django/kos/static/"
```

## Init database

```bash
docker-compose up -d
# enter the postgres shell
docker exec -it kos_postgres psql -U postgres

# in postgres shell:
create database kos_db;
create user kos with password 'password1234';
grant all privileges on database kos_db to kos;
\q # or Ctrl+d

docker-compose down
```

## Apply migrations on empty database
```bash
docker-compose up -d
docker exec -it kos_django python manage.py migrate
docker-compose down
```

## Add super user for django
```bash
docker-compose up -d
docker exec -it kos_django python manage.py createsuperuser
docker-compose down
```

