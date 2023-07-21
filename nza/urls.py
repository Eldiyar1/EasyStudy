from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include
router = DefaultRouter()
router.register(r'random-idiom', IdiomViewSet)
router.register(r'random-quote', QuoteViewSet)


urlpatterns = [
    *router.urls,
    path('antonyms/', AntonymView.as_view(), name='antonyms'),
    path('synonyms/', SynonymView.as_view(), name='synonyms'),
    path('search/<str:keyword>/', PhotoSearchView.as_view()),
    path('', include(router.urls)),
]