from django.shortcuts import render

# Create your views here.
from django.views import View
from django.shortcuts import render, redirect
from .models import Resume
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseBadRequest
from .forms import NewResumeForm
# Create your views here.
class ResumeListView(View):
    def get(self, request, *args, **kwargs):
        context = {'resumes': Resume.objects.all()}
        return render(request, 'resume/list.html', context=context)

class NewResumeView(View):
    def get(self, request, *args, **kwargs):
        context = {'add_resume_form': NewResumeForm}
        return render(request, 'resume/create.html', context=context)

    def post(self, request, *args, **kwargs):
        is_authenticated = request.user.is_authenticated

        if not is_authenticated:
            raise PermissionDenied

        form = NewResumeForm(request.POST)

        if not form.is_valid():
            return HttpResponseBadRequest('<h1>400 Bad Request</h1>')

        author = request.user
        description = form.cleaned_data['description']
        Resume.objects.create(author=author, description=description)
        return redirect('/resumes')
