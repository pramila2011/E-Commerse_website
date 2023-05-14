from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import random 
from django.conf import settings
from .models import *

# Create your views here.
def home (request):
    return render(request,'index.html', {'index': 'active'})

def album (request):
    return render(request,'album.html', {'album': 'active'})

def blog (request):
    return render(request,'blog.html', {'blog': 'active'})

def mail (request):
    return render(request,'mail.html', {'mail': 'active'})

def single (request):
    return render(request,'single.html', {'single': 'active'})

def typo (request):
    return render(request,'typo.html', {'typo': 'active'})

def register (request):
    return render(request,'register.html')

def register_submit(request):
    
    if request.POST['passwd'] == request.POST['repasswd']:
        global g_otp, user_data
        user_data = [request.POST['first_name'], 
                     request.POST['last_name'],
                     request.POST['user_name'],
                     request.POST['email'],
                     request.POST['passwd']]
        g_otp = random.randint(100000, 999999)
        send_mail('Welcome Welcome',
                  f"Your OTP is {g_otp}",
                  settings.EMAIL_HOST_USER,
                  [request.POST['email']])
        return render(request, 'otp.html')        
    else:
        return render(request, 'register.html', {'msg': 'Both passwords do not MATCH'})
    
def otp_fun(request):
    try:
        if int(request.POST['u_otp']) == g_otp:
            User.objects.create(
                first_name = user_data[0],
                    last_name = user_data[1],
                    username = user_data[2],
                    email = user_data[3],
                    password = user_data[4])
            return render(request, 'register.html', {'msg':'Successfully Registered!!'})
        else:
            return render(request, 'otp.html', {'msg': 'Invalid OTP, Enter again!!!'})
    except:
        return render(request, 'register.html')
    


def login(request):
    if request.method == 'GET' :
        return render(request,'login.html')
    else:
           
        try:
           
            r1 = User.objects.get(email = request.POST['email'])
  
            if request.POST['passwd'] == r1.password:
                request.session['user_email'] = request.POST['email']
                return render(request, 'index.html', {'userdata': r1, 'home' : 'jivit'})
            else:
                return render(request, 'login.html', {'msg': 'Invalid password'})
        except:
            return render(request, 'login.html', {'msg':'email is not registered!!'})
       
def logout(request):
             
             del request.session['user_email']
             return render(request, 'index.html', {'home': 'active'})