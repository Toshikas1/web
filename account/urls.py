"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.http import HttpResponse
from .views import login1, register, logout1, profile, edit, change_password

urlpatterns = [ 
    path("login/", login1, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout1, name="logout"),
    path("profile/", profile, name="profile"),
    path("profile/edit/", edit, name="profile_edit"),
    path("profile/change_password/", change_password, name="change_password")
]