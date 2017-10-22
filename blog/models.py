from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    Title = models.CharField(max_length=32)
    Content = models.TextField()

    # def __unicode__(self):
    #     return self.Title


# Create your models here.
