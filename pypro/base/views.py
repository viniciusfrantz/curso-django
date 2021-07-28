# Create your views here.
# 1
from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')
