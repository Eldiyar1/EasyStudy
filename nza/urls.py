from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include
router = DefaultRouter()
router.register(r'random-idiom', IdiomViewSet)
router.register(r'random-quote', QuoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

