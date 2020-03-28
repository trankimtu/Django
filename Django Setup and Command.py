# pip install django 
# python -m django --version
# list subcommand: django-admin
    # django-admin startproject <project name>: create a new django project
# Start server: python manage.py runserver 
# 127.0.0.1:8000 = localhost:8000 (127.0.0.1 = localhost)
# localhost:8000/admin 

# 1 project can have many apps, like components
# to create a new app: python manage.py startapp <app name>

import django
print(django.__version__)