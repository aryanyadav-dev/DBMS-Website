from unicodedata import category
from django.shortcuts import render ,get_object_or_404 ,redirect
from .models import *  # noqa: F403
from django.http import FileResponse
from .models import Filepdf
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import os

def homepage(request):
    return render(request,'./index.html')

def download_file(request, id):
    files = get_object_or_404(Filepdf, pk=id)
    file_path = files.file.path
    response = FileResponse(open(file_path,'rb'))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = f'attachment; filename="{files.title}.pdf"'
    return response

def PPT(request):
    files = Filepdf.objects.filter(category = "PPT")
    context = {
        'files' : files
    }
    return render(request, './ppt.html',context)

def Study(request):
    files = Filepdf.objects.filter(category="Study Material")
    context = {
        'files' : files
    }
    return render(request, './Studymaterial.html',context)

def Practicals(request):
    files = Filepdf.objects.filter(category="Practicals")
    context = {
        'files' : files
    }
    return render(request, './Practicals.html',context)

def Module(request):
    files = Filepdf.objects.filter(category="Resource book")
    context = {
        'files' : files
    }
    return render(request, './Modules.html',context)

def PYQ(request):
    files = Filepdf.objects.filter(category="Question paper") | Filepdf.objects.filter(category="Answer Book")
    context = {
        'files' : files
    }
    return render(request, './PYQ.html',context)

def trail(request):
    return render(request,'./trial.html')