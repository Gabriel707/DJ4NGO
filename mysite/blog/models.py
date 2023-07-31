from django.db import models
from django.utils import timezone

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250) # short label
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True) # DOB of post / Data de criação do post
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                                choices=Status.choices,
                                default=Status.DRAFT)

    # Defining metadata / definindo metadado para o model
    class Meta: 
        order = ['-publish']  
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title