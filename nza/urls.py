from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

router = DefaultRouter()
router.register(r'random-idiom', IdiomViewSet)
router.register(r'random-quote', QuoteViewSet)
router.register(r'word_translate', WordTranslateViewSet)
router.register(r'chapter', ChapterViewSet)
category_detail = CategoryWordViewSet.as_view({'get': 'words_by_category', 'post': 'create'})


urlpatterns = [
    *router.urls,
    path('antonyms/', AntonymView.as_view(), name='antonyms'),
    path('synonyms/', SynonymView.as_view(), name='synonyms'),
    path('grammar/', GrammarViewSet.as_view(), name='grammar'),
    path('question/', QuestionListView.as_view(), name='question'),
    path('search/<str:keyword>/', PhotoSearchView.as_view()),
    path('', include(router.urls)),
]

