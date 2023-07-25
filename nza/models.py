from django.db import models
from jsonfield import JSONField


class Quote(models.Model):
    text = models.TextField()


class Idiom(models.Model):
    text = models.TextField()


class Photo(models.Model):
    keyword = models.CharField(max_length=100)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)


class Grammar(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    test = models.JSONField(max_length=255)
    json = JSONField()

    def __str__(self):
        return self.title
