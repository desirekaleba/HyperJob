from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from vacancy.forms import NewVacancyForm
from resume.forms import NewResumeForm


# Create your views here.
class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'hyperjob/main.html', context={})


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'hyperjob/signup.html'


class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'hyperjob/login.html'


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = NewVacancyForm() if request.user.is_staff else NewResumeForm()
        context = {
            'form': form,
            'is_authenticated': request.user.is_authenticated,
            'is_staff': request.user.is_staff,
            'username': request.user.username,
        }
        return render(request, 'hyperjob/home.html', context=context)
