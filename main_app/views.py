# Django Imports
from django.shortcuts import render
from django.http import HttpResponse

# Standard Package Imports

# Project Imports
from .models import *

# Third Party Imports


# Create your views here.
def home(request):
    
    services = Service.objects.all()
    projects = Project.objects.all()
    faqs = Faq.objects.all()
    prices = Price.objects.all()
    members = Member.objects.all()

    context = {
        'services': services,
        'faqs': faqs,
        'prices': prices,
        'members': members,
        'projects': projects,
    }

    return render(request, 'home.html', context)

def viewmembers(request):
    
    
    members = Member.objects.all()

    context = {
        
        'members': members,
        
    }

    return render(request, 'viewMembers.html', context)

def members(request, name):
    member = Member.objects.get(name=name)
    context = {
        'member': member,
    }
    return render(request, 'members.html', context)

def temp(request):
    return render(request, 'members.html', {})

def viewMembers(request):
    return render(request, 'viewMembers.html', {})

def publications(request):
    return render(request, 'publications.html', {})

def form(request):
    return render(request, 'form.html', {})