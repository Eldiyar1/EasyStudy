from django.contrib import admin
from .models import Example, Quote, Idiom, Chapter, Subsection, Question, Grammar, Listening, Word


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ('example',)
    search_fields = ('example',)


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'author')
    search_fields = ('text', 'author')


@admin.register(Idiom)
class IdiomAdmin(admin.ModelAdmin):
    list_display = ('text',)
    search_fields = ('text',)


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    pass


@admin.register(Subsection)
class SubsectionAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'correct_answer_index')
    search_fields = ('text',)


@admin.register(Grammar)
class GrammarAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter', 'subsection')
    list_filter = ('chapter', 'subsection')
    search_fields = ('title', 'description')


@admin.register(Listening)
class ListeningAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('word',)
    search_fields = ('word',)