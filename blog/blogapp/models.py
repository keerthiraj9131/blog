from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager


#class Custommodel(models.Manager):
   # def get_queryset(self):
    #    return super().get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (('draft', 'DRAFT'), ('published', 'Published'))
    title=models.CharField(max_length=30)
    slug = models.SlugField(max_length=256,unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_post',on_delete=models.DO_NOTHING)
    publish =models.DateTimeField(default=timezone.now)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    #objects=Custommodel()
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('postdetail',args=[self.publish.year,
                                          self.publish.strftime('%m'),
                                          self.publish.strftime('%d'),
                                          self.slug])
class proxymodel(Post):
    class Meta:
        proxy = True

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=20)
    email= models.EmailField()
    body = models.TextField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering =('-created',)
