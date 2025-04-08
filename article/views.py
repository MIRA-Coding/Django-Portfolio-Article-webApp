from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Article, Tag

# Create your views here.

def render_article(request):
    # Fetch all articles and tags from the database
    posts = Article.objects.all()
    tags = Tag.objects.all()

    # Adding context data to pass to the template
    context = {
        'page_title': 'Articles Page',
        'posts': posts,  # Pass the articles to the template
        'tags': tags,    # Pass the tags to the template
    }
    return render(request, 'articles.html', context)




