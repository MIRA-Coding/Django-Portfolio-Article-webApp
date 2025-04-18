"""
URL configuration for Main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from article import views
from Portfolio import views as portfolio_views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.render_article, name='render_article'), 
    path('', portfolio_views.render_portf, name='render_portf'),  
    path('subscribe/', views.subscribe, name='subscribe'),
    path('mainStory/', views.mainStory, name='mainStory'),
    path('articles/fetch_all/', views.fetch_all_articles, name='fetch_all_articles'),
    path('articles/<str:article_title>/', views.render_generated_article, name='render_generated_article'),
    path('main-story/', views.mainStory, name='mainStory'),  

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)