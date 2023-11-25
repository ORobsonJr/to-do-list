from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class LOGIN(TemplateView):
    template_name = 'login.html'

