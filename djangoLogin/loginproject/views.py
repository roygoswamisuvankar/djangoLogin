from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import employee
from django.db import connection
from .models import student
from django.contrib.sessions.models import Session

#holding home page
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        #id = request.POST.get()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        pwd = request.POST.get('pass')
        if student.objects.filter(email=email).count():
            sms = 'Please enter unique email address'
            return render(request, 'index.html', { 'sms' : sms })
        else:
            data_save = student(name=name, phone=phone, email=email, password = pwd)
            data_save.save()
            sms = 'Data saved successfully'
            return render(request, 'index.html', { 'sms' : sms })
    return render(request,'index.html')

def home(request):
    if 'check_logged' in request.session:
        current_user = request.session['check_logged']
        param = { 'current_user' : current_user }
        return render(request, 'home.html', param)
    else:
        return redirect('index')
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pass')
        check_user = student.objects.filter(email = email, password = pwd)
        if check_user:
            request.session['check_logged'] = email
            return redirect('home')
        else:
            sms = 'invalid username and password'
            return render(request, 'index.html', { 'sms' : sms })
        return render(request, 'index.html')

def home2(request):
    if 'check_logged' in request.session:
        current_user = request.session['check_logged']
        param = {'current_user': current_user}
        return render(request, 'home2.html', param)
    else:
        return redirect('index')
    return render(request, 'index.html')

def logout(request):
    try:
        del request.session['check_logged']
    except:
        return redirect('index')
    return redirect('index')