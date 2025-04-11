from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Article, Tag
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.db.models import Q

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

def subscribe(request):
    context = {
        'page_title': 'Subscribe',
    }
    return render(request, 'subscribe.html')

def mainStory(request):
    context = {
        'page_title': 'Main Story',
    }
    return render(request, 'mainStory.html')




def render_generated_article(request, article_title):
    # Replace hyphens with spaces to match the title in the database
    formatted_title = article_title.replace('-', ' ')
    
    # Fetch the article instance by title
    instance = get_object_or_404(Article, title=formatted_title)
    
    # Pass the article instance to the template
    context = {
        'instance': instance,
        
    }
    return render(request, f"generated_articles/{article_title}.html", context)




def search_articles(request):
    query = request.GET.get('q', '')  # Get the search query
    if query:
        # Filter articles by title
        posts = Article.objects.filter(title__icontains=query)
    else:
        # Return all articles if no query
        posts = Article.objects.all()

    # Render the same template with filtered posts
    return render(request, 'articles.html', {'posts': posts})