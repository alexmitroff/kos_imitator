# KOS imitator based on django

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

