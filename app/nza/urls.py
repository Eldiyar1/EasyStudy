from rest_framework.routers import DefaultRouter
from .views import IdiomViewSet, QuoteViewSet, WordTranslateViewSet, AntonymViewSet, SynonymViewSet, GrammarViewSet, \
    SectionViewSet, SubsectionViewSet, ListeningViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'word_translate', WordTranslateViewSet, basename='word_translate')
router.register(r'idiom', IdiomViewSet, basename='idiom')
router.register(r'quote', QuoteViewSet, basename='quote')
router.register(r'synonym', SynonymViewSet, basename='synonym')
router.register(r'antonyms', AntonymViewSet, basename='antonym')
router.register(r'section', SectionViewSet)
router.register(r'subsection', SubsectionViewSet)
router.register(r'grammar', GrammarViewSet, basename='grammar')
router.register(r'listening', ListeningViewSet)

urlpatterns = [
    *router.urls,
    path('', include(router.urls)),
]

