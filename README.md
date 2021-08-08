# First Project
Django web api using Django REST Framework. This is my first django project.

## Setup

1. Clone the repository:

```cmd
git clone https://github.com/ngoc-phuc/django_first_project.git
cd first_project
```

2. Install Python 3.9.6

3. Install postgree, then run:
```cmd
pip install psycopg2
```

4. Install Django

```cmd
py -m pip install Django

py -m pip install colorama

pip install djangorestframework
```
5. Change your database config at `first_project/setting.py` ,then migrate the database

```sh
python manage.py makemigrations

py manage.py migrate
```

Finally:
```sh
py manage.py runserver
```
And navigate to `http://127.0.0.1:8000/api/users/`.
