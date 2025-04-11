from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import os

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True)
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)  # Add this field


    def __str__(self):
        return self.title
    

@receiver(post_save, sender=Article)
def create_article_html(sender, instance, created, **kwargs):
    if created:  # Only create the HTML file when a new article is added
        # Define the directory where the HTML file will be saved
        articles_dir = os.path.join(settings.BASE_DIR, 'article', 'templates', 'generated_articles')
        os.makedirs(articles_dir, exist_ok=True)  # Create the directory if it doesn't exist

        # Define the file path (replace spaces with hyphens)
        file_path = os.path.join(articles_dir, f"{instance.title.replace(' ', '-').lower()}.html")

        # Generate the HTML content with template notations
        html_content = f"""
        {{% extends "base.html" %}}

        {{% block content %}}
        <div class="container my-5">
            <div class="row justify-content-center">
                <div class="col-lg-8 col-md-10">
                  <img src="{{{{ instance.image.url }}}}" alt="" style="aspect-ratio: 16 / 9; object-fit: cover; width: 100%;">          

                    <article class="p-4">
                        <header class="mb-4 px-4">
                            <h1 class="text-start pt-5">{{{{ instance.title }}}}</h1>
                            <p class="text-muted text-start pb-5">By {{{{ instance.author }}}} | Published on {{{{ instance.created_at|date:"F d, Y" }}}}</p>
                        </header>
                        <article>
                            <section class="text-body-emphasis text-start" style="font-size: 1.25rem; line-height: 1.8; padding: 2rem; max-width: 800px; margin: auto;">
                                <p>
                                    {{{{ instance.content|safe }}}}
                                </p>
                            </section>
                        </article>
                    </article>
                </div>
            </div>
        </div>
        {{% endblock %}}
        """

        # Write the HTML content to the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)