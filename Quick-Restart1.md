# Quickly Restarting Over Fifty Five Project
## Description
The goal of this article is to provide instructions on how to quickly format the project and restart it, if you have previously installed it successfully.

## Instructions
### MacOS Database

  ```sql
  drop database comicscantina_db;
  create database comicscantina_db;
  \c comicscantina_db;
  CREATE USER django WITH PASSWORD '123password';
  GRANT ALL PRIVILEGES ON DATABASE comicscantina_db to django;
  ALTER USER django CREATEDB;
  ALTER ROLE django SUPERUSER;
  CREATE EXTENSION postgis;
  ```

### Ubuntu Database

  ```sql
  sudo -i -u postgres
  psql

  DROP DATABASE comicscantina_db;
  CREATE DATABASE comicscantina_db;
  \c comicscantina_db;
  CREATE USER django WITH PASSWORD '123password';
  GRANT ALL PRIVILEGES ON DATABASE comicscantina_db to django;
  ALTER USER django CREATEDB;
  ALTER ROLE django SUPERUSER;
  CREATE EXTENSION postgis;
  ```

### CentOS 7 Database:

  ```sql
  sudo -i -u postgres;
  dropdb comicscantina_db;
  createdb comicscantina_db;
  psql comicscantina_db;
  CREATE USER django WITH PASSWORD '123password';
  GRANT ALL PRIVILEGES ON DATABASE comicscantina_db to django;
  ALTER USER django CREATEDB;
  ALTER ROLE django SUPERUSER;
  CREATE EXTENSION postgis;
  ```

### Restart Script
Just copy and paste this into your command console.

```bash
python manage.py makemigrations; \
python manage.py migrate_schemas; \
python manage.py init_app; \
python manage.py populate_site; \
python manage.py populate_public; \
python manage.py create_shared_account "bart@email.com" "123password" "Bart" "Mika"; \
python manage.py create_franchise "london" "Over55" "Over55 (London) Inc." "Located at the Forks of the Thames in downtown London Ontario, Over 55 is a non profit charitable organization that applies business strategies to achieve philanthropic goals. The net profits realized from the services we provide will help fund our client and community programs. When you use our services and recommended products, you are helping to improve the quality of life of older adults and the elderly in our community." "CA" "London" "Ontario" "" "N6H 1B4" "78 Riverside Drive" ""; \
python manage.py create_tenant_account "london" 2 "bart+m@email.com" "123password" "Bart" "Mika" "123 123-1234" "" "123 123-1234" "CA" "London" "Ontario" "" "N6H 1B4" "78 Riverside Drive" "";
```

Optional:

```bash
python manage.py run_historic_csv_import_for_tenant "london" "prod"
```
