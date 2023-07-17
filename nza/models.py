from django.db import models


# Create your models here.

class Quote(models.Model):
    text = models.TextField()


class Idiom(models.Model):
    text = models.TextField()
