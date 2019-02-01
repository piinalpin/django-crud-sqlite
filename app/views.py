from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import App_Student

# Create your views here.

class StudentList(ListView):
    model = App_Student

class StudentDetail(DetailView):
    model = App_Student

class StudentCreate(CreateView):
    model = App_Student
    fields = ['name', 'identityNumber', 'address', 'department']
    success_url = reverse_lazy('student_list')

class StudentUpdate(UpdateView):
    model = App_Student
    fields = ['name', 'identityNumber', 'address', 'department']
    success_url = reverse_lazy('student_list')

class StudentDelete(DeleteView):
    model = App_Student
    success_url = reverse_lazy('student_list')