from django.db import models


class Antonym(models.Model):
    word = models.CharField(max_length=100)
    antonyms = models.JSONField()

    class Meta:
        verbose_name = "Антоним"
        verbose_name_plural = "Антонимы"

    def __str__(self):
        return self.word


class Synonym(models.Model):
    word = models.CharField(max_length=100)
    synonym = models.JSONField()

    class Meta:
        verbose_name = "Cиноним"
        verbose_name_plural = "Синонимы"

    def __str__(self):
        return self.word


class Quote(models.Model):
    text = models.TextField(
        max_length=255,
        verbose_name='Введите цитату:')
    author = models.TextField(
        max_length=50,
        verbose_name='Автор:')

    class Meta:
        verbose_name = "Цитаты"
        verbose_name_plural = "Цитаты"

    def __str__(self):
        return self.text


class Idiom(models.Model):
    text = models.TextField(
        max_length=255,
        verbose_name='Введите идиому')

    class Meta:
        verbose_name = "Идиомы"
        verbose_name_plural = "Идиомы"

    def __str__(self):
        return self.text



class Chapter(models.Model):
    chapter = models.CharField(
        max_length=255,
        verbose_name='Раздел')

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Раздел"

    def __str__(self):
        return self.chapter


class Subsection(models.Model):
    subsection = models.CharField(max_length=255, verbose_name='Подраздел')

    class Meta:
        verbose_name = "Подраздел"
        verbose_name_plural = "Подраздел"

    def __str__(self):
        return self.subsection


class Question(models.Model):
    text = models.CharField(max_length=255, verbose_name='Текст:')
    answer_1 = models.CharField(max_length=100, verbose_name='Ответ 1:')
    answer_2 = models.CharField(max_length=100, verbose_name='Ответ 2:')
    answer_3 = models.CharField(max_length=100, verbose_name='Ответ 3:')
    answer_4 = models.CharField(max_length=100, verbose_name='Ответ 4:')
    correct_answer_index = models.PositiveSmallIntegerField(
        choices=[(1, 'Answer 1'), (2, 'Answer 2'), (3, 'Answer 3'), (4, 'Answer 4')]
        , verbose_name='Правильный ответ:')

    def incorrect_answers(self):
        return [
            self.answer_1,
            self.answer_2,
            self.answer_3,
            self.answer_4,
        ]

    class Meta:
        verbose_name = "Tест"
        verbose_name_plural = "Тест"

    def __str__(self):
        return self.text


class Grammar(models.Model):
    chapter = models.ForeignKey(
        Chapter,
        on_delete=models.CASCADE,
        verbose_name='Раздел')
    subsection = models.ForeignKey(
        Subsection,
        on_delete=models.CASCADE,
        default=1,
        blank=True,
        null=True,
        verbose_name='Подраздел')
    title = models.CharField(
        max_length=200,
        verbose_name='Введите тему:')
    description = models.TextField(
        verbose_name='Введите описание темы:')
    test = models.ManyToManyField(Question, verbose_name='Тест')

    class Meta:
        verbose_name = "Грамматика"
        verbose_name_plural = "Грамматика"

    def __str__(self):
        return self.title


class Listening(models.Model):
    title = models.CharField(max_length=255, verbose_name='Аудирование')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = "Аудирование"
        verbose_name_plural = "Аудирование"

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
    category = models.ForeignKey(Category,null=True,  on_delete=models.CASCADE, verbose_name='Категория')
    word = models.CharField(max_length=100,  verbose_name='Слово')

    class Meta:
        verbose_name = "Слова"
        verbose_name_plural = "Слова"
