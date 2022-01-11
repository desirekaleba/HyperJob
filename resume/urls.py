from django.urls import path
from . import views

urlpatterns = [
    path("", views.ResumeListView.as_view()),
    path("new", views.NewResumeView.as_view())
]
