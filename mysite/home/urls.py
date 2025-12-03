from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('students/',views.student_list, name='my_students'),
    path('teachers/',views.teachers_list, name='teachers'),
    path('create/',views.)
]   