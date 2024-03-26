# SOD
StockODiary Website

# How to set up
fork the repo
download your forked repo
create a branch

# OS Dependencies

# Ubuntu

sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib

# create a database

sudo -u postgres psql
CREATE DATABASE sdiarydos;

# go to SOD/core/settings.py and update db credentials as per your settings

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'sod', 
            'USER': 'postgres', 
            'PASSWORD': 'somepassword',
            'HOST': '127.0.0.1', 
            'PORT': '5432',
        },
}

# open terminal in root SOD dir location

# create a python environment
python -m venv .venv --prompt "SOD"
source .venv/bin/activate

# make db migrations
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

# run server
python manage.py runserver 0.0.0.0:8000

# open the browser 
http://localhost:8000/