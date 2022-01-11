from django.urls import path
from . import views

urlpatterns = [
    path("", views.VacancyListView.as_view()),
    path("new", views.NewVacancyView.as_view())
]
