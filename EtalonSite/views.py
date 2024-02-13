from django.shortcuts import render
from django.views.generic import TemplateView
import datetime
from .models import *

def page_not_found_view(request, exception):
    return render(request, 'EtalonSite/404.html', status=404)

def base(request):
    today = datetime.datetime.now().date()
    
    return render(request, 'EtalonSite/base.html', {"today" : today})

def home(request):
    massMedia = MassMedia.objects.all()
    vacancies = Vacancies.objects.all()
    services = Services.objects.all()
    today = datetime.datetime.now().date()

    return render(request,'EtalonSite/home.html',{"vacancies":vacancies,"today" : today,'massMedia': massMedia,'services':services})

def blog(request):
    massMedia = MassMedia.objects.all()
    today = datetime.datetime.now().date()

    return render(request,'EtalonSite/blog.html',{"today" : today,'massMedia': massMedia})

def galery(request):
    return render(request,'EtalonSite/galery.html')

def video(request):
    return render(request,'EtalonSite/video.html')

def vacancies(request):
    vacancies = Vacancies.objects.all()
    today = datetime.datetime.now().date()

    return render(request,'EtalonSite/vacancies.html',{"vacancies":vacancies,"today" : today})

def contacts(request):
    pdf_cart = pdfCart.objects.first()
    today = datetime.datetime.now().date()

    return render(request,'EtalonSite/contacts.html',{"today" : today,"pdf_cart":pdf_cart})


