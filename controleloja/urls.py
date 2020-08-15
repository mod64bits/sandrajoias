from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.core import urls as core_url
from apps.cliente import urls as cliente_url

urlpatterns = [
    path('', include(core_url)),
    path('cliente/', include(cliente_url)),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
