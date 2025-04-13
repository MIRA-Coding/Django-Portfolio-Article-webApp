from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Article, Tag
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt


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


@csrf_exempt
def fetch_all_articles(request):
    # Fetch all articles from the database
    articles = Article.objects.all()
    results = [
        {
            'title': article.title,
            'content': article.content[:100],  # Limit content to 100 characters
            'created_at': article.created_at.strftime('%B %d, %Y'),
            'url': f"/articles/{article.title.replace(' ', '_')}/",
            'image': article.image.url if article.image else None,
        }
        for article in articles
    ]
    return JsonResponse({'articles': results})