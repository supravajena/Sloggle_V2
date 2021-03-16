"""Sloggle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from SloggleUI.views import home, find_jobs, hire_freelancer, post_project, about, contact, post_project_details, activate, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('find_jobs', find_jobs, name="find_jobs"),
    path('hire_freelancer', hire_freelancer, name="hire_freelancer"),
    path('post_project', post_project, name="post_project"),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('post_project_details', post_project_details, name="post_project_details"),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('register', register, name = "register")
]
