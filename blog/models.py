from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

from users.models import UserProfile

CATEGORIES = [
        ("FE", 'Frontend'),
        ("BE", 'Backend'),
        ("FS", 'Fullstack'),
    ]
STATUS = [
        ("DR", 'Draft'),
        ("PUB", 'Published'),
    ]


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=300)
    image = models.ImageField(upload_to='pictures/', blank=True, null=True)
    category = models.CharField(max_length=3, choices=CATEGORIES, default="FE")
    status = models.CharField(max_length=3, choices=STATUS, default="DR")
    

    def __str__(self):
        return f"{self.title}"

    class Meta :
        ordering = ['category']
        verbose_name_plural = 'Gönderiler'

