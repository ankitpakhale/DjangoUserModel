mkdir django-custom-user-model && cd django-custom-user-model
python3 -m venv env
source env/bin/activate

pip install django
django-admin startproject PROJECTNAME
cd PROJECTNAME
python manage.py startapp APPNAME
python manage.py migrate
python manage.py runserver
