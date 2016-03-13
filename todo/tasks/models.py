from __future__ import unicode_literals
from django.forms import ModelForm
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
# Create your models here.


class task(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(task, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class taskForm(ModelForm):
    class Meta:
        model = task
        fields = ['name', 'description', 'tags']
