from django.shortcuts import render
from datetime import datetime

# Create your views here.

def acceuil(request):
    return render(request, 'front/acceuil.html', locals())
