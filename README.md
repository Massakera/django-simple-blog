# Django Blog Project

This is a simple blogging platform built with Django to test some features. It allows users to create, edit, and delete posts. Comments can be added to each post.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### set up a python virtual env

```bash
python -m venv venv
source venv/bin/activate
```

### Install requirements

```bash
pip install -r requirements.txt
```

### Make migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create the super user

```bash
python manage.py createsuperuser
```

### Run the server

```bash
python manage.py runserver
```

