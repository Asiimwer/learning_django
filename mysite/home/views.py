from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'home/index.html')

def contact(request):
    return HttpResponse("Contact us on 0758349017")

def about(request):
    return render(request,'home/about.html' )

# Create your views here.
