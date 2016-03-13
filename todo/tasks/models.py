from __future__ import unicode_literals

from django.db import models
from taggit.managers import TaggableManager
# Create your models here.

class task(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created = models.DateTimeField()
    tags = TaggableManager()

    def __str__(self):
        return self.name