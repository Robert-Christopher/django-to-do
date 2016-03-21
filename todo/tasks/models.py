from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
# Create your models here.

class Tagmap(models.Model):
    task = models.ForeignKey('Task')
    tag = models.ForeignKey('Tag')
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    
class Task(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, through='Tagmap')

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.name