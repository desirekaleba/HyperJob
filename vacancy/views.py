from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponseForbidden
from .models import Vacancy

from .forms import NewVacancyForm


# Create your views here.
class VacancyListView(View):
    def get(self, request, *args, **kwargs):
        context = {'vacancies': Vacancy.objects.all()}
        return render(request, 'vacancy/list.html', context=context)


class NewVacancyView(View):
    def get(self, request, *args, **kwargs):
        context = {'add_vacancy_form': NewVacancyForm}
        return render(request, 'vacancy/create.html', context=context)

    def post(self, request, *args, **kwargs):
        is_manager = request.user.is_staff
        is_authenticated = request.user.is_authenticated

        if not is_manager or not is_authenticated:
            return HttpResponseForbidden('<h1>Forbidden</h1>')

        form = NewVacancyForm(request.POST)

        if not form.is_valid():
            return HttpResponseBadRequest('<h1>400 Bad Request</h1>')

        author = request.user
        description = form.cleaned_data['description']
        Vacancy.objects.create(author=author, description=description)
        return redirect('/vacancies')
