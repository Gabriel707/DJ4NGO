from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250) # short label
    author = models.ForeignKey(User,                        # Create relationship between users and posts
                               on_delete=models.CASCADE,
                               related_name="blog_posts") 

    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True) # DOB of post / Data de criação do post
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                                choices=Status.choices,
                                default=Status.DRAFT)

    # Defining metadata / definindo metadado para o model
    class Meta: 
        ordering = ['-publish']  
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title