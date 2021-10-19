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

def members(request, name):
    member = Member.objects.get(name=name)
    context = {
        'member': member,
    }
    return render(request, 'members.html', context)

def temp(request):
    return render(request, 'members.html', {})

def viewmembers(request):
    members = Member.objects.all()
    context = {
        'members': members,
    }
    return render(request, 'viewmembers.html', context)

def form1(request):
    if request.method == 'POST':
        name=request.POST.get('fname')
        email = request.POST.get('email')
        mobile=request.POST.get('mobile')
        country = request.POST.get('country')
        subject = request.POST.get('subject')
        deadline = request.POST.get('trip-start')
        timezone = request.POST.get('appt-time')
        topic = request.POST.get('topic')
        oins= request.POST.get('w3review')
        price= request.POST.get('price')
        pcode= request.POST.get('pcode') 
        data={
            'name':name,
            'email':email,
            'mobile':mobile,
            'country':country,
            'subject':subject,
            'deadline':deadline,
            'timezone':timezone,
            'topic':topic,
            'oins':oins,
            'price':price,
            'pcode':pcode,
        }
        print(data)
        html_content='Name: ' + name + '<br>Mobile: ' + mobile + '<br>Country: ' + country + '<br>Deadline: ' + deadline+ '<br>Time: ' + timezone + '<br>Topic: ' + topic + '<br>Other Instructions: ' + oins + '<br>Price: ' + price + '<br>Promocode: ' + pcode 
        file1=request.FILES['file1']
        file2=request.FILES['file2']
        file3=request.FILES['file3']
        file4=request.FILES['file4']
        msg=EmailMessage(data['subject'], html_content, 'testttesting37@gmail.com',['testttesting37@gmail.com'])
        msg.content_subtype = "html"
        msg.attach(file1.name,file1.read(),file1.content_type)
        msg.attach(file2.name,file2.read(),file2.content_type)
        msg.attach(file3.name,file3.read(),file3.content_type)
        msg.attach(file4.name,file4.read(),file4.content_type)
        msg.send()
    else:
        print('nope')
    return render(request, 'form1.html')

def subjects(request,name):
    subject = Subjects.objects.get(name=name)
    context = {
        'subject': subject,
    }
    print(subject)
    return render(request, 'subjects.html', context)
