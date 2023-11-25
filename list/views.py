from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class LOGIN(TemplateView):
    template_name = 'login.html'

class INDEX(TemplateView):
    template_name = 'index.html'