from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

from shohada import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
]

# --- Add Static Files --- #
if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

