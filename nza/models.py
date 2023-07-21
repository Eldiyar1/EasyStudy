from django.db import models


# Create your models here.

class Quote(models.Model):
    text = models.TextField()


class Idiom(models.Model):
    text = models.TextField()


class Photo(models.Model):
    keyword = models.CharField(max_length=100)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)