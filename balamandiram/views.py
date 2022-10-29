from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    return render(request, 'balamandiram/home.html')

def gallery(request):
    return render(request, 'balamandiram/gallery.html', {'posts': Gallery.objects.all().order_by('-id')})

def library(request):
    return render(request, 'balamandiram/library.html')

def scibooks(request):
    books = Libraray.objects.filter(genre='Science')
    return render(request, 'balamandiram/scibooks.html', {'books': books})

def langbooks(request):
    books = Libraray.objects.filter(genre='Languages')
    return render(request, 'balamandiram/languages.html', {'books': books})

def childlit(request):
    books = Libraray.objects.filter(genre='Children Literature')
    return render(request, 'balamandiram/childlit.html', {'books': books})

def mags(request):
    books = Libraray.objects.filter(genre='Magazines')
    return render(request, 'balamandiram/mags.html', {'books': books})

def activities(request):
    return render(request, 'balamandiram/activities.html')
