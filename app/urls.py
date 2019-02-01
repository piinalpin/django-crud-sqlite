from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentList.as_view(), name='student_list'),
    path('view/<int:pk>', views.StudentDetail.as_view(), name='student_detail'),
    path('new', views.StudentCreate.as_view(), name='student_new'),
    path('edit/<int:pk>', views.StudentUpdate.as_view(), name='student_edit'),
    path('delete/<int:pk>', views.StudentDelete.as_view(), name='student_delete'),
]