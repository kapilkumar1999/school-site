# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render
def index(request):
    return render(request,'school/index.html')

# Create your views here.
def admission(request):
    return render(request,'school/admission.html')
def activities_work(request):
    return render(request,'school/activities_work.html')
def principalmessage(request):
    return render(request,'school/principalmessage.html')
def Reachus(request):
    return render(request,'school/Reachus.html')
def rulesregulations(request):
    return render(request,'school/rulesregulations.html')
def gallery(request):
    return render(request,'school/gallery.html')
def student(request):
    return render(request,'school/student.html')
def teacher(request):
    return render(request,'school/teacher.html')

