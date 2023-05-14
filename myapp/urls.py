from django.urls import path, include
from .views import *    

urlpatterns = [
    path('',home,name='home'),
    path('album/',album,name='album'),
    path('blog/',blog,name='blog'),
    path('mail/',mail,name='mail'),
    path('single/',single,name='single'),
    path('typo/',typo,name='typo'),
    path('register/',register,name='register'),
    path('register_submit/',register_submit,name='register_submit'),
    path('otp/', otp_fun, name='otp'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

]
    