# Dev

create a django project called  ‘company’ and application called ‘staff’?
 
django-admin startproject company
cd company
django-admin startapp staff

INSTALLED_APPS = ( 
 # [...]
 staff,
 )

Python manage.py makemigrations
Python manage.py migrate

python manage.py createsuperuser
 
Python manage.py runserver

