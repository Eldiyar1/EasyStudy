from django.contrib import admin
from django.urls import path, include
from english_backend.settings.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nza.urls'))
]

urlpatterns += doc_urls