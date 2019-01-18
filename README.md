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
5. Create the model to define the table structure of database and save the collection into database `app/models.py`
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
6. Every after change `models.py` you need to make migrations into `db.sqlite3` (database) to create the table for the new model
```
manage.py makemigrations
manage.py migrate
```
7. Create the views to create app pages on browser, the file is `app/views.py` according the above structure
```python
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Student

# Create your views here.

class StudentList(ListView):
    model = Student

class StudentDetail(DetailView):
    model = Student

class StudentCreate(CreateView):
    model = Student
    # Field must be same as the model attribute
    fields = ['name', 'identityNumber', 'address', 'department']
    success_url = reverse_lazy('student_list')

class StudentUpdate(UpdateView):
    model = Student
    # Field must be same as the model attribute
    fields = ['name', 'identityNumber', 'address', 'department']
    success_url = reverse_lazy('student_list')

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')
```
8. Then, create file `app/urls.py` to define app url path (in CI as same as route function)
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentList.as_view(), name='student_list'),
    path('view/<int:pk>', views.StudentDetail.as_view(), name='student_detail'),
    path('new', views.StudentCreate.as_view(), name='student_new'),
    path('edit/<int:pk>', views.StudentUpdate.as_view(), name='student_edit'),
    path('delete/<int:pk>', views.StudentDelete.as_view(), name='student_delete'),
]
```
9. The `app/urls.py` would not work unless you include that into the main url `rattlesnake/urls.py`
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    :
    path('student/', include('app.urls')),
    :
]
```
10. Create the html file to display user interface, you need create directory `app/templates/app/` like below
```
* django-crud-sqlite/
  |--- rattlesnake/
  |    |--- app/
  |    |    |--- migrations/
  |    |    |--- templates/
  |    |    |    |--- app/
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
11. Create file `app/templates/app/student_list.html` to display or parsing student list data with `ListView` library
```html
<h1>Student List</h1>
<a href="{% url 'student_new' %}">Create New Student</a><br><br>
<table border="1">
    <tr>
        <th>Name</th>
        <th>Identity Number</th>
        <th>Action</th>
    </tr>
    {% for student in object_list %}
    <tr>
        <td>{{ student.name }}</td>
        <td>{{ student.identityNumber }}</td>
        <td>
            <a href="{% url 'student_detail' student.id %}">Detail</a>
            <a href="{% url 'student_edit' student.id %}">Edit</a>
            <a href="{% url 'student_delete' student.id %}">Delete</a>
        </td>
    </tr>
    {% empty %}
    <tr><td colspan="3"><b>Data is empty! Please, add data first.</b></td></tr>
    {% endfor %}
</table>
```
12. Create file `app/templates/app/student_detail.html` to display or parsing data of each student and will used by `DetailView` library
```html
<h1>Student Detail</h1>
<h3>Name : {{ object.name }}</h3>
<h3>Identity Number : {{ object.identityNumber }}</h3>
<h3>Address : {{ object.address }}</h3>
<h3>Department : {{ object.department }}</h3>
```
13. Create file `app/templates/app/student_form.html` to display form input and edit views
```html
<h1>Student Form</h1>
<form method="POST">{% csrf_token %}
    <table>
        <tr>
            <td>Name</td>
            <td>:</td>
            <td>{{ form.name }}</td>
        </tr>
        <tr>
            <td>Identity Number</td>
            <td>:</td>
            <td>{{ form.identityNumber }}</td>
        </tr>
        <tr>
            <td>Department</td>
            <td>:</td>
            <td>{{ form.department }}</td>
        </tr>
        <tr>
            <td>Address</td>
            <td>:</td>
            <td>{{ form.address }}</td>
        </tr>
        <tr>
            <td><input type="submit" value="Save"></td>
        </tr>
    </table>
</form>
```
14. Create file `app/templates/app/student_confirm_delete.html` to display promt or alert confirmation to delete the object view
```html
<form method="post">{% csrf_token %}
    Are you sure you want to delete "{{ object }}" ?
    <input type="submit" value="Submit" />
</form>
```
15. Test the project
```
manage.py runserver
```

### After change structure of flask project
```
* django-crud-sqlite/
  |--- rattlesnake/
  |    |--- app/
  |    |    |--- migrations/
  |    |    |--- templates/
  |    |    |    |--- app/
  |    |    |    |    |--- student_confirm_delete.html
  |    |    |    |    |--- student_detail.html
  |    |    |    |    |--- student_form.html
  |    |    |    |    |--- student_list.html
  |    |    |--- __init__.py
  |    |    |--- admin.py
  |    |    |--- apps.py
  |    |    |--- models.py
  |    |    |--- tests.py
  |    |    |--- urls.py
  |    |    |--- views.py
  |    |--- rattlesnake/
  |    |    |--- __init__.py
  |    |    |--- settings.py
  |    |    |--- urls.py
  |    |    |--- wsgi.py
  |    |--- db.sqlite3
  |    |--- manage.py
  |--- venv/
```

### Running service screenshot

1. List student page but if list is empty will display `Data is empty! Please add data first.`
![Sample 1](https://raw.githubusercontent.com/piinalpin/django-crud-sqlite/master/docs/1.PNG)

2. Form input student page, url path `student/new`
![Sample 2](https://raw.githubusercontent.com/piinalpin/django-crud-sqlite/master/docs/2.PNG)

3. List student page if data inserted
![Sample 3](https://raw.githubusercontent.com/piinalpin/django-crud-sqlite/master/docs/3.PNG)

![Sample 4](https://raw.githubusercontent.com/piinalpin/django-crud-sqlite/master/docs/4.PNG)

4. Student detail page, url path `student/view/<parameters:id>`
![Sample 5](https://raw.githubusercontent.com/piinalpin/django-crud-sqlite/master/docs/5.PNG)

![Sample 6](https://raw.githubusercontent.com/piinalpin/django-crud-sqlite/master/docs/6.PNG)

5. Form edit student page, url path `student/edit/<parameter:id>
![Sample 7](https://raw.githubusercontent.com/piinalpin/django-crud-sqlite/master/docs/7.PNG)

![Sample 8](https://raw.githubusercontent.com/piinalpin/django-crud-sqlite/master/docs/8.PNG)

6. Confirmation page if data will remove from collection, url path `student/delete/<parameter:id>`
![Sample 9](https://raw.githubusercontent.com/piinalpin/django-crud-sqlite/master/docs/9.PNG)

![Sample 10](https://raw.githubusercontent.com/piinalpin/django-crud-sqlite/master/docs/10.PNG)

## Built With

* [Python 3](https://www.python.org/download/releases/3.0/) - The language programming used
* [Django 2](https://www.djangoproject.com/) - The web framework used
* [Virtualenv](https://virtualenv.pypa.io/en/latest/) - The virtual environment used
* [SQLite 3](https://www.sqlite.org/index.html) - The database library

## Clone or Download

You can clone or download this project
```
> Clone : git clone https://github.com/piinalpin/django-crud-sqlite.git
```

## Authors

* **Alvinditya Saputra** - *Initial work* - [DSS Consulting](https://dssconsulting.id/) - [LinkedIn](https://linkedin.com/in/piinalpin) [Instagram](https://www.instagram.com/piinalpin) [Twitter](https://www.twitter.com/piinalpin)
