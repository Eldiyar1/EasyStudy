from rest_framework.routers import DefaultRouter
from .views import (IdiomViewSet, QuoteViewSet, WordTranslateViewSet, AntonymViewSet, SynonymViewSet, ListeningViewSet,
                    QuestionViewSet, SectionListViewSet, SubsectionListViewSet, GrammarListViewSet, ExampleViewSet)
from django.urls import path, include

router = DefaultRouter()

viewsets = [
    (WordTranslateViewSet, 'word_translate'),
    (IdiomViewSet, 'idiom'),
    (QuoteViewSet, 'quote'),
    (SynonymViewSet, 'synonym'),
    (AntonymViewSet, 'antonym'),
    (SectionListViewSet, 'section_list'),
    (SubsectionListViewSet, 'subsection_list'),
    (GrammarListViewSet, 'grammar_list'),
    (ExampleViewSet, 'example'),
    (QuestionViewSet, 'question'),
    (ListeningViewSet, 'listening'),
]

for viewset, basename in viewsets:
    router.register(f'{basename}', viewset, basename=basename)

urlpatterns = [
    path('', include(router.urls)),
]
