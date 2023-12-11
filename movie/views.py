from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def browseindex(request):
    filmler=Movie.objects.all()
    context={
        "filmler":filmler
    }
    return render(request, 'browse-index.html',context)