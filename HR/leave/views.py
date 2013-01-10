# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render 
from leave.models import employees
def home(request):
    return HttpResponse("Welcome to my e-leave application.")

def detail_employee(request,employee_id):
    return HttpResponse("you are at employee page number %s." % employee_id)

def all(request):
    emp=employees.objects.all()
    return render(request,'leave/all.html',{'emp':emp})
