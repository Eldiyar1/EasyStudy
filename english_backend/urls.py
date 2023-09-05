from django.contrib import admin
from django.urls import path, include
from .settings.yasg import urlpatterns_swagger as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.nza.urls'))
]

urlpatterns += doc_urls