from django.db import models

from app.nza.constants import ANSWER_CHOICES


class Example(models.Model):
    example = models.TextField(verbose_name='Пример: ')

    class Meta:
        verbose_name = "2. Пример"
        verbose_name_plural = "2. Примеры"

    def __str__(self):
        return self.example


class Section(models.Model):
    section = models.CharField(max_length=255, verbose_name='Раздел')

    class Meta:
        verbose_name = "3. Раздел"
        verbose_name_plural = "3. Разделы"

    def __str__(self):
        return self.section


class Subsection(models.Model):
    subsection = models.CharField(max_length=255, verbose_name='Подраздел')
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING, related_name="subsection", null=True, blank=True)

    class Meta:
        verbose_name = "4. Подраздел"
        verbose_name_plural = "4. Подразделы"

    def __str__(self):
        return self.subsection


class Grammar(models.Model):
    title = models.CharField(max_length=200, verbose_name='Введите тему:')
    description = models.TextField(verbose_name='Введите описание темы:')
    subsection = models.ForeignKey(Subsection, on_delete=models.DO_NOTHING, related_name="grammar")
    example = models.ForeignKey(Example, on_delete=models.CASCADE, verbose_name='Пример: ', related_name="grammar")

    class Meta:
        verbose_name = "5. Грамматика"
        verbose_name_plural = "5. Грамматика"

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.CharField(max_length=255, verbose_name='Текст:')
    answer_1 = models.CharField(max_length=100, verbose_name='Ответ 1:')
    answer_2 = models.CharField(max_length=100, verbose_name='Ответ 2:')
    answer_3 = models.CharField(max_length=100, verbose_name='Ответ 3:')
    answer_4 = models.CharField(max_length=100, verbose_name='Ответ 4:')
    correct_answer_index = models.PositiveSmallIntegerField(choices=ANSWER_CHOICES, verbose_name='Правильный ответ:')
    grammar = models.ForeignKey(Grammar, on_delete=models.DO_NOTHING, related_name="question")

    class Meta:
        verbose_name = "1. Tест"
        verbose_name_plural = "1. Тесты"

    def __str__(self):
        return self.text


class Word(models.Model):
    word = models.CharField(max_length=100, verbose_name='Слово')

    class Meta:
        verbose_name = "6. Слово"
        verbose_name_plural = "6. Слова"


class Idiom(models.Model):
    text = models.TextField(max_length=255, verbose_name='Введите идиому')

    class Meta:
        verbose_name = "7. Идиома"
        verbose_name_plural = "7. Идиомы"

    def __str__(self):
        return self.text


class Quote(models.Model):
    text = models.TextField(max_length=255, verbose_name='Введите цитату:')
    author = models.TextField(max_length=50, verbose_name='Автор:')

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
    word = models.CharField(max_length=100)
    synonym = models.JSONField()

    class Meta:
        verbose_name = "Cиноним"
        verbose_name_plural = "Синонимы"

    def __str__(self):
        return self.word


class Antonym(models.Model):
    word = models.CharField(max_length=100)
    antonym = models.JSONField()

    class Meta:
        verbose_name = "Антоним"
        verbose_name_plural = "Антонимы"

    def __str__(self):
        return self.word
