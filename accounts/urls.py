from django.urls import path, include
from accounts import views

# app_name =  "accounts"
urlpatterns= [
   
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'), 
    path('logout/', views.logout, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('terms/', views.terms, name='terms'),
    path('home/', views.home, name='home'),
    path('grading/', views.grading, name='grading'),
    path('services/', views.services, name='services'),
    path('talk/', views.talk, name='talk'),
    path('rate/', views.rate, name='rate'),
    path('order/', views.order, name='order'),
    path('daniel/', views.daniel, name='daniel'),
    path('isaiah/', views.isaiah, name='isaiah'),
    path('zephy/', views.zephy, name='zephy'),
    path('kate/', views.kate, name='kate'),
    path('orderlist/', views.orderlist, name='orderlist'),
    path('tutorsignup/', views.tutorsignup, name='tutorsignup'), 
    
    path('employee/', views.employee, name='employee'), 
    path('list/', views.list, name='list'), 


]