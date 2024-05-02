from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def members(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')