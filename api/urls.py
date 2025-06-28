from django.urls import path
from .views import HolidayListView
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('holidays/', HolidayListView.as_view()),
]
