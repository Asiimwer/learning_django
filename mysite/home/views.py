from django.shortcuts import render
from django.http import HttpResponse
from home.models import MyStudent
from home.models import Teachers

def index(request):
    return render(request, 'home/index.html')

def contact(request):
    return HttpResponse("Contact us on 0758349017")

def about(request):
    return render(request,'home/about.html' )

def student_list(request):
    students = MyStudent.objects.all()
    return render(request,'home/students.html',{'students':students})

# Create your views here.
