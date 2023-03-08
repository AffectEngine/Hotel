from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/v1/drf_auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('', include('PGapp.urls')),
	path('accounts/', include('allauth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()

if settings.DEBUG:
	import debug_toolbar
	urlpatterns = [
		path('__debug__/', include(debug_toolbar.urls)),
	] + urlpatterns
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)