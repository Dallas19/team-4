from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('students/<int:student_id>', views.student, name = 'match-student'),
    path('students', views.students, name='match-students'),
    path('companies', views.companies, name='match-companies')
]