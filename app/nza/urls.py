from rest_framework.routers import DefaultRouter
from .views import (
    IdiomViewSet, QuoteViewSet, WordTranslateViewSet, AntonymViewSet,
    SynonymViewSet, GrammarViewSet, SectionViewSet, SubsectionViewSet,
    ListeningViewSet, ExampleViewSet, QuestionViewSet
)
from django.urls import path, include

router = DefaultRouter()

viewsets = [
    (WordTranslateViewSet, 'word_translate'),
    (IdiomViewSet, 'idiom'),
    (QuoteViewSet, 'quote'),
    (SynonymViewSet, 'synonym'),
    (AntonymViewSet, 'antonym'),
    (SectionViewSet, 'section'),
    (SubsectionViewSet, 'subsection'),
    (ExampleViewSet, 'example'),
    (GrammarViewSet, 'grammar'),
    (QuestionViewSet, 'question'),
    (ListeningViewSet, 'listening'),
]

for viewset, basename in viewsets:
    router.register(f'{basename}', viewset, basename=basename)

urlpatterns = [
    path('', include(router.urls)),
]