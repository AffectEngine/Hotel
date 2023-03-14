from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/v1/drf_auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('', include('PGapp.urls')),
	path('accounts/', include('allauth.urls')),
	path('api/v1/auth/', include('djoser.urls')),
	re_path(r'^auth/', include('djoser.urls.authtoken')),
	path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()

if settings.DEBUG:
	import debug_toolbar
	urlpatterns = [
		path('__debug__/', include(debug_toolbar.urls)),
		path('static/<path:path>', never_cache(serve)),
	] + urlpatterns
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)