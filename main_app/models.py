from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Movement(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='movement_image',
                              default='default.png')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

