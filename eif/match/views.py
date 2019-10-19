from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, match")

def company(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def student(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def job(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
