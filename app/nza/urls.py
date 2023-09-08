from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include


router = DefaultRouter()
router.register(r'idiom', IdiomViewSet, basename='idiom')
router.register(r'quote', QuoteViewSet, basename='quote')
router.register(r'word_translate', WordTranslateViewSet, basename='word_translate')
router.register(r'antonyms', AntonymViewSet, basename='antonym')
router.register(r'synonym', SynonymViewSet, basename='synonym')
router.register(r'grammar', GrammarViewSet, basename='grammar')
router.register(r'chapters', ChapterViewSet)
router.register(r'subsections', SubsectionViewSet)

urlpatterns = [
    *router.urls,
    path('', include(router.urls)),
]

