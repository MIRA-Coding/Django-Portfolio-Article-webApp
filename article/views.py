from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def render_article(request):
    # Adding context data to pass to the template
    context = {
        'page_title': 'Articles Page',
        'tabs': [
            {'id': 'home', 'title': 'Home', 'content': 'Welcome to the Home tab!'},
            {'id': 'profile', 'title': 'Profile', 'content': 'This is your Profile tab content.'},
            {'id': 'dropdown1', 'title': 'Dropdown 1', 'content': 'Content for Dropdown 1.'},
            {'id': 'dropdown2', 'title': 'Dropdown 2', 'content': 'Content for Dropdown 2.'},
        ]
    }
    return render(request, 'articles.html', context)
