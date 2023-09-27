import nltk
from django.db import models

from app.nza.constants import ANSWER_CHOICES

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')


class Section(models.Model):
    section = models.CharField(max_length=255, verbose_name='Раздел')

    class Meta:
        verbose_name = "1. Раздел"
        verbose_name_plural = "1. Разделы"

    def __str__(self):
        return self.section


class Subsection(models.Model):
    subsection = models.CharField(max_length=255, verbose_name='Подраздел')
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, related_name="subsection",
                                verbose_name='Раздел')

    class Meta:
        verbose_name = "2. Подраздел"
        verbose_name_plural = "2. Подразделы"

    def __str__(self):
        return self.subsection


class Grammar(models.Model):
    title = models.CharField(max_length=200, verbose_name='Введите тему:')
    description = models.TextField(verbose_name='Введите описание темы:')
    subsection = models.ForeignKey(Subsection, on_delete=models.SET_NULL, null=True, related_name="grammar",
                                   verbose_name='Подраздел')

    class Meta:
        verbose_name = "3. Грамматика"
        verbose_name_plural = "3. Грамматика"

    def __str__(self):
        return self.title


class Example(models.Model):
    example = models.TextField(verbose_name='Пример: ')
    grammar = models.ForeignKey(Grammar, on_delete=models.SET_NULL, null=True, related_name="example",
                                verbose_name='Грамматика')

    class Meta:
        verbose_name = "4. Пример"
        verbose_name_plural = "4. Примеры"

    def __str__(self):
        return self.example


class Question(models.Model):
    text = models.CharField(max_length=255, verbose_name='Текст:')
    answer_1 = models.CharField(max_length=100, verbose_name='Ответ 1:')
    answer_2 = models.CharField(max_length=100, verbose_name='Ответ 2:')
    answer_3 = models.CharField(max_length=100, verbose_name='Ответ 3:')
    answer_4 = models.CharField(max_length=100, verbose_name='Ответ 4:')
    correct_answer_index = models.PositiveSmallIntegerField(choices=ANSWER_CHOICES, verbose_name='Правильный ответ:')
    grammar = models.ForeignKey(Grammar, on_delete=models.SET_NULL, null=True, related_name="question",
                                verbose_name='Грамматика')

    class Meta:
        verbose_name = "5. Tест"
        verbose_name_plural = "5. Тесты"

    def __str__(self):
        return self.text


class Word(models.Model):
    word = models.CharField(max_length=100, verbose_name='Слово')

    class Meta:
        verbose_name = "6. Слово"
        verbose_name_plural = "6. Слова"


class Idiom(models.Model):
    text = models.CharField(max_length=255, verbose_name='Введите идиому:')

    class Meta:
        verbose_name = "7. Идиома"
        verbose_name_plural = "7. Идиомы"

    def __str__(self):
        return self.text


class Quote(models.Model):
    text = models.CharField(max_length=255, verbose_name='Введите цитату:')
    author = models.CharField(max_length=50, verbose_name='Автор:')

    class Meta:
        verbose_name = "8. Цитата"
        verbose_name_plural = "8. Цитаты"

    def __str__(self):
        return self.text


class Listening(models.Model):
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = "9. Аудирование"
        verbose_name_plural = "9. Аудирование"

    def __str__(self):
        return self.text


class Synonym(models.Model):
    word = models.CharField(max_length=100, verbose_name='Слово')
    synonym = models.CharField(max_length=100, verbose_name='Синоним')

    class Meta:
        verbose_name = "Cиноним"
        verbose_name_plural = "Синонимы"

    def __str__(self):
        return self.word


class Antonym(models.Model):
    word = models.CharField(max_length=100, verbose_name='Слово')
    antonym = models.CharField(max_length=100, verbose_name='Антоним')

    class Meta:
        verbose_name = "Антоним"
        verbose_name_plural = "Антонимы"

    def __str__(self):
        return self.word