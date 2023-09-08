from django.contrib import admin
from .models import *

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'author')
    search_fields = ('text', 'author')


class IdiomAdmin(admin.ModelAdmin):
    list_display = ('text',)
    search_fields = ('text',)


class ChapterAdmin(admin.ModelAdmin):
    pass


class SubsectionAdmin(admin.ModelAdmin):
    pass

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'correct_answer_index')
    search_fields = ('text',)


class ExampleAdmin(admin.ModelAdmin):
    list_display = ('example',)
    search_fields = ('example',)


class GrammarAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter', 'subsection')
    list_filter = ('chapter', 'subsection')
    search_fields = ('title', 'description')


class ListeningAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


class WordAdmin(admin.ModelAdmin):
    list_display = ('word',)
    search_fields = ('word',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Example, ExampleAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Idiom, IdiomAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Subsection, SubsectionAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Grammar, GrammarAdmin)
admin.site.register(Listening, ListeningAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(Category, CategoryAdmin)
