from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/', include('common.api.urls')),
    path('api/', include('groups.api.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
