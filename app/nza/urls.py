from rest_framework.routers import DefaultRouter
from .views import (
    IdiomViewSet, QuoteViewSet, WordTranslateViewSet, AntonymViewSet,
    SynonymViewSet,
# GrammarViewSet, SectionViewSet, SubsectionViewSet,
    ListeningViewSet, ExampleViewSet, QuestionViewSet, SectionListViewSet, SubsectionListViewSet, GrammarListViewSet
)
from django.urls import path, include

router = DefaultRouter()

viewsets = [
    (WordTranslateViewSet, 'word_translate'),
    (IdiomViewSet, 'idiom'),
    (QuoteViewSet, 'quote'),
    (SynonymViewSet, 'synonym'),
    (AntonymViewSet, 'antonym'),
    # (SectionViewSet, 'section'),
    (SectionListViewSet, 'section_list'),
    # (SubsectionViewSet, 'subsection'),
    (SubsectionListViewSet, 'subsection_list'),
    (ExampleViewSet, 'example'),
    # (GrammarViewSet, 'grammar'),
    (GrammarListViewSet, 'grammar_list'),
    (QuestionViewSet, 'question'),
    (ListeningViewSet, 'listening'),
]

for viewset, basename in viewsets:
    router.register(f'{basename}', viewset, basename=basename)

urlpatterns = [
    path('', include(router.urls)),
]