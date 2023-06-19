from django.db import models

from taggit.managers import TaggableManager
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=10000)
    publish = models.BooleanField(default=False)
    image = models.ImageField(upload_to='posts')
    tags = TaggableManager()

# title
# content
# author
# image
# tags
