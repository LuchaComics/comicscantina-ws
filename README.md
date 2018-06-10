pip install django                        # Our MVC Framework
pip install django-environ                # Environment Variables with 12factorization
pip install Pillow                        # Req: ImageField
pip install django-cors-headers           # Enable CORS in Headers
pip install gunicorn                      # Web-Server Helper
pip install djangorestframework           # RESTful API Endpoint Generator
pip install django-starterkit             # Django starter kit
pip install django_filter                 # Filter querysets dynamically
pip install django-oauth-toolkit
pip install Requests-OAuthlib             # OAuthlib support for Python-Requests!
#pip install djangorestframework-msgpack   # MessagePack support for Django REST framework
#pip install djangorestframework-jwt       # JSON Web Token Authentication support for Django REST Framework


drop database comicscantina_db;
create database comicscantina_db;
\c comicscantina_db;
CREATE USER django WITH PASSWORD '123password';
GRANT ALL PRIVILEGES ON DATABASE comicscantina_db to django;
ALTER USER django CREATEDB;
ALTER ROLE django SUPERUSER;
CREATE EXTENSION postgis;


python manage.py makemigrations; \
python manage.py migrate_schemas; \
python manage.py init_app; \
python manage.py populate_site; \
python manage.py populate_public;
