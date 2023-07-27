from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

router = DefaultRouter()
router.register(r'random-idiom', IdiomViewSet)
router.register(r'random-quote', QuoteViewSet)
router.register(r'grammar', GrammarViewSet)
router.register(r'word_translate', WordTranslateViewSet)

category_list = CategoryViewSet.as_view({'get': 'list', 'post': 'create'})
category_detail = CategoryWordViewSet.as_view({'get': 'words_by_category', 'post': 'create'})
antonym = WordAntonymViewSet.as_view({'get': 'antonyms'})
synonym = WordSynonymViewSet.as_view({'get': 'list'})

urlpatterns = [
    *router.urls,
    path('antonyms/', AntonymView.as_view(), name='antonyms'),
    path('synonyms/', SynonymView.as_view(), name='synonyms'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('words/<int:pk>/antonyms/', antonym, name='word-antonyms'),
    path('words/<int:pk>/synonyms/', synonym, name='word-synonyms'),
    path('category_detail/<int:pk>/', category_detail),
    path('category_list/', category_list),
    path('search/<str:keyword>/', PhotoSearchView.as_view()),
    path('', include(router.urls)),
]

