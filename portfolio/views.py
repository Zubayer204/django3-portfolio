from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()
    payload = {'projects': projects}
    return render(request, 'portfolio/home.html', payload)
