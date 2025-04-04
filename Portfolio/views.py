from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def render_portf(request):
    return render(request, 'home.html')
