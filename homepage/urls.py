# from django.contrib import admin
from homepage import views
from django.urls import path, include




from django.contrib.auth import views as auth_views
urlpatterns = [
    path('home/', views.loadhome, name='home'),
    path('contact/', views.loadcontact, name='contact'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('register/', views.register, name='register'),
    path('register_submit/', views.register_submit, name='register_submit'),
    path('successRegister/', views.successRegister, name='successRegister'),
    path('success/', views.success, name='success'),
    path('success/home/', views.success, name='success'),
    path('', views.loadhome, name='home'),



    path('login_submit/', views.login_submit, name='login_submit'),
    path('login/', auth_views.LoginView.as_view(), name='login'),#need a specific view auth here
    # path('contact/submit/', views.contact_submit, name='contact_submit'),
]