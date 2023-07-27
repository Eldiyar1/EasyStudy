from django.db import models
from jsonfield import JSONField
from django.contrib.auth.models import User


class Quote(models.Model):
    text = models.TextField()


class Idiom(models.Model):
    text = models.TextField()


class Photo(models.Model):
    keyword = models.CharField(max_length=100)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True, null=True,
        verbose_name="фотография пользователя"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    statistics = models.TextField(
        blank=True,
        verbose_name="Статика"
    )
    achievements = models.TextField(
        blank=True,
        verbose_name="Достижения"
    )

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


class Grammar(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    test = models.JSONField(max_length=255)
    json = JSONField()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Word(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
