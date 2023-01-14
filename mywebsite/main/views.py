from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')

def demand(request):
    return render(request, 'main/demand.html')

def geography(request):
    return render(request, 'main/geography.html')

def skills(request):
    return render(request, 'main/skills.html')

def latestVac(request):
    return render(request, 'main/latestVac.html')