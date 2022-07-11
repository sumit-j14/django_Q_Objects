from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# importing Q
from django.db.models import Q


# Create your views here.
def get_all(request):
    students = Student.objects.all()
    for student in students:
        print(student.name)
    return HttpResponse("check console")


def get_rollnumber(request, rn):
    print(rn)
    student = Student.objects.get(roll_number=rn)
    print(student.name)
    return HttpResponse("check console")


# using q objects
def qsearch(request, rn, an):
    print(rn, type(rn))
    print(an, type(an))
    try:
        students = Student.objects.filter(Q(roll_number=rn) & Q(admission_number=an))
        for student in students:
            print(student)
    except Exception as e:
        print(e)
    return HttpResponse("check console")
