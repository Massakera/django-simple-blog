from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published_date__lte=timezone.now())

    def recent_posts(self):
        return self.order_by('-published_date')[:5]  # Adjust the number as needed


# Custom manager that extends models.Manager
class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def recent_posts(self):
        return self.get_queryset().recent_posts()

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    objects = PostManager()
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
