from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import *
from match.fetch import get_match_info
from match.matching.matching import match

# Create your views here.
def index(request):
    return HttpResponse("Hello, match")

def companies(request):
    companies = Company.objects.order_by('company_name')
    context = {'companies': companies}
    return render(request, 'match/companies.html', context)

def student(request, student_id, job_id):
    student = get_object_or_404(Student, pk=student_id)
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'match/student.html', {'student': student}, {'job': job})

def students(request):
    students = Student.objects.order_by('last_name')
    context = {'students': students}
    return render(request, 'match/students.html', context)

def match_interviews(request):
    jobs, students = get_match_info()
    # 2 is max number of students that can be interviewed for a position
    match_results = match(jobs, students, 2)
    print(match_results)
    return render(request, 'match/match_results.html')

