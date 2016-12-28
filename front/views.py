from django.shortcuts import render
from datetime import datetime
from .forms import ContacteForm

# Create your views here.

def acceuil(request):
    return render(request, 'front/acceuil.html', locals())

def coordonnees(request):
    return render(request, 'front/coordonnees.html', locals())

def contact(request):
    form = ContacteForm()
    return render(request, 'front/contact.html', {'form': form})
