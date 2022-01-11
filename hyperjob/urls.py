"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.MainView.as_view()),
    path("vacancies/", include("vacancy.urls")),
    path("resumes/", include("resume.urls")),
    path("vacancy/", include("vacancy.urls")),
    path("resume/", include("resume.urls")),
    path("signup", views.SignupView.as_view()),
    path("login", views.LoginView.as_view()),
    path("logout", LogoutView.as_view()),
    path("home", views.HomeView.as_view()),
    path("login/", RedirectView.as_view(url="/login")),
    path("signup/", RedirectView.as_view(url="/signup"))
]
