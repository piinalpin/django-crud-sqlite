# Django CRUD App With SQLite (Python 3)
### Codename : Rattlesnake

Tutorial for building create, retrieve, update and delete website application with Django and SQLite (default django database)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Make sure you have installed Python 3 and virtual environment on your device

### Project structure
File structure in django by default has a structure like below
```
* django-crud-sqlite/
  |--- rattlesnake/
  |    |--- app/
  |    |    |--- migrations/
  |    |    |--- templates/
  |    |    |--- __init__.py
  |    |    |--- admin.py
  |    |    |--- apps.py
  |    |    |--- models.py
  |    |    |--- tests.py
  |    |    |--- views.py
  |    |--- rattlesnake/
  |    |    |--- __init__.py
  |    |    |--- settings.py
  |    |    |--- urls.py
  |    |    |--- wsgi.py
  |    |--- manage.py
  |--- venv/
```

### Step to create django crud

A step by step series of examples that tell you how to get a development env running

1. Create virtual environment and activate inside your `django-crud-sqlite/` directory according the above structure
```
virtualenv venv
> On windows -> venv\Scripts\activate
> On linux -> . env/bin/activate
```
2. Install django and start new project inside your `django-crud-sqlite/` directory according the above structure
```
pip install django
django-admin startproject rattlesnake
cd rattlesnake
```
3. Create new app, from `rattlesnake/` directory will create create new `app/` to store the collection
```
> On Windows -> manage.py startapp app
> On Linux, etc -> ./manage.py startapp app
```
4. Register your app into `rattlesnake` project, the `app` to `INSTALLED_APP` in `rattlesnake/settings.py`
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    :
    'app',
    :
]
```
5. Create the model to save the collection into database `app/models.py`
```python
from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200, null=False)
    identityNumber = models.CharField(max_length=200, null=False)
    address = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
    # The absolute path to get the url then reverse into 'student_edit' with keyword arguments (kwargs) primary key
    def get_absolute_url(self):
        return reverse('student_edit', kwargs={'pk': self.pk})
```
