from django.contrib import admin
from .models import Example, Quote, Idiom, Section, Subsection, Question, Grammar, Listening, Word


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('section',)
    search_fields = ('section',)


@admin.register(Subsection)
class SubsectionAdmin(admin.ModelAdmin):
    list_display = ('subsection',)
    search_fields = ('subsection',)


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('word',)
    search_fields = ('word',)


@admin.register(Grammar)
class GrammarAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'correct_answer_index')
    search_fields = ('text', 'answer_1', 'answer_2', 'answer_3', 'answer_4')


@admin.register(Idiom)
class IdiomAdmin(admin.ModelAdmin):
    list_display = ('text',)
    search_fields = ('text',)


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'author')
    search_fields = ('text', 'author')


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ('example',)
    search_fields = ('example',)


@admin.register(Listening)
class ListeningAdmin(admin.ModelAdmin):
    list_display = ('text',)
    search_fields = ('text',)
