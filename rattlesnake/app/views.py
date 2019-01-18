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
    fields = ['name', 'identityNumber']
    success_url = reverse_lazy('student_list')

class StudentUpdate(UpdateView):
    model = Student
    fields = ['name', 'identityNumber']
    success_url = reverse_lazy('student_list')

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')