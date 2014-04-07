from django.shortcuts import render

# incluimos una vista generica
from django.views.generic import TemplateView

class IndexView(TemplateView):
	template_name = 'home/index.html'