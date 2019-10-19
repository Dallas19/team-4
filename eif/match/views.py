from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return HttpResponse("Hello, match")

def companies(request):
    companies = Company.objects.order_by('company_name')
    context = {'companies': companies}
    return render(request, 'match/companies.html', context)

def student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'match/student.html', {'student': student})

def students(request):
    students = Student.objects.order_by('last_name')
    context = {'students': students}
    return render(request, 'match/students.html', context)
