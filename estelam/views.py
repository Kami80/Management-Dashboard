from django.shortcuts import render, redirect
from django.db.models import Q
from .models import File, Materials, Companies

# Create your views here.

def page(request):
    
    posts = File.objects.all().order_by("-date_created")

    return render(request, 'index.html', {'posts':posts})

def searchmaterials(request):
    mats = Materials.objects.all()
    return render(request, 'materials.html', {'materials':mats})

def searchcompanies(request):
    comps = Companies.objects.all()
    return render(request, 'companies.html', {'companies':comps})