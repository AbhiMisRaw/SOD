License
Unless specified otherwise, sod is released under the Apache 2.0 except for the code related to UI templates in folder frontend. 

However the code used for UI is not open source and must be purchased from the below url:
https://prium.github.io/phoenix/v1.14.0/showcase.html
https://themes.getbootstrap.com/product/phoenix-admin-dashboard-webapp-template/

All rights related UI templates kit and source code related to templates kit belongs with owner listed in above urls.
Please contact and purchases licenses as applicable before you use the application in the production.


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
CREATE DATABASE sod;
\q

# Navigate to repo
cd SOD

# create a python environment
python3 -m venv .venv --prompt "SOD"
source .venv/bin/activate
pip install -r requirements.txt 

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

# create .env file
sudo nano .env

# add below config variables to .env file
SOD_ENV="dev"
DB_PASSWORD="ChangeMe"

# first save the changes
CTRL+O
ENTER

# exit nano
CTRL+X


# make db migrations
python manage.py migrate

python manage.py createsuperuser

# run server
python manage.py runserver 0.0.0.0:8000

# open the browser 
http://localhost:8000/
