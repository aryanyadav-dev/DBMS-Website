from unicodedata import category
from django.shortcuts import render ,get_object_or_404 ,redirect
from .models import *  # noqa: F403
from django.http import FileResponse
from .models import Filepdf , User_Admin
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

def admin(request):
    if request.user.is_anonymous:
        messages.error(request,"You are not authorized to view this page. Please login first.")
        return redirect('login')

    files = Filepdf.objects.all()
    context = {
        "files" : files
    }
    return render(request,'./admin.html',context)

def update(request,id):
    file = Filepdf.objects.get(id = id)
    if request.method == "POST":
        file.title = request.POST.get('title')
        file.category = request.POST.get('category')
        file.description = request.POST.get('description')
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            if file.file:
                if os.path.exists(file.file.path): 
                    os.remove(file.file.path)
            file.file = uploaded_file
        file.save()
        return redirect('admin')
    else:
        context = {
            'file': file
        }
        return render(request, './update.html', context)

def delete_file(request,id):
    file = Filepdf.objects.get(id=id)
    file.delete()
    return redirect('admin')

def create_file(request):
    if request.method == "POST":
        Title = request.POST['title']
        Discription = request.POST['description']
        Category = request.POST['category']
        uploaded_file = request.FILES['file']

        Filepdf.objects.create(title=Title,disc=Discription,category=Category,file=uploaded_file)
        return redirect('admin')

    return render(request, './create.html')

def trail(request):
    return render(request,'./trial.html')

def logout_user(request):
    logout(request)
    return redirect('homepage')


def login_user(request):
    if request.method == "POST":
        username_user = str(request.POST['Name'])
        password_user = str(request.POST['password'])
        user = authenticate(username=username_user,password=password_user)
        if user :
            login(request,user)
            return redirect('admin')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('login')
    
    return render(request,'./login.html')