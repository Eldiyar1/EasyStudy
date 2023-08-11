from django.db import models
from jsonfield import JSONField
from django.contrib.auth.models import User


class Quote(models.Model):
    text = models.TextField(
        max_length=255,
        verbose_name='Введите цитату:')

    class Meta:
        verbose_name = "Цитаты"
        verbose_name_plural = "Цитаты"


class Idiom(models.Model):
    text = models.TextField(
        max_length=255,
        verbose_name='Введите идиому:')

    class Meta:
        verbose_name = "Идиомы"
        verbose_name_plural = "Идиомы"


class Photo(models.Model):
    keyword = models.CharField(
        max_length=100,
        verbose_name='Введите слово:')
    image_url = models.URLField(
        verbose_name='Ссылка на фото:')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"


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


class Chapter(models.Model):
    chapter = models.CharField(
        max_length=255,
        verbose_name='Раздел')

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Раздел"


class Grammar(models.Model):
    chapter = models.ForeignKey(
        Chapter,
        on_delete=models.CASCADE,
        default=1,
        blank=True,
        null=True,
        verbose_name='Времена')
    title = models.CharField(
        max_length=200,
        verbose_name='Введите тему:')
    description = models.TextField(
        max_length=255,
        verbose_name='Введите описание темы:')
    test = models.JSONField(
        max_length=255,
        null=True, blank=True,
        verbose_name='Тест:')
    json = JSONField(null=True, blank=True)


    class Meta:
        verbose_name = "Грамматика"
        verbose_name_plural = "Грамматика"

    def __str__(self):
        return self.title


class Category(models.Model):
    category = models.CharField(
        max_length=100,
        verbose_name='Категории:')

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.category


class Word(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    word = models.CharField(max_length=100, verbose_name='Слово')

    class Meta:
        verbose_name = "Слова"
        verbose_name_plural = "Слова"
