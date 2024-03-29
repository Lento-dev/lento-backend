from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="LENTO API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    re_path(r'^api/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^api/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^api/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/account/', include('user_account.api.urls')),
    path('api/social-auth/', include('drf_social_oauth2.urls',namespace='drf')),
    path('api/advertisement/', include('advertisement.api.urls')),
    path('api/sentry-debug/', trigger_error),
    
]
if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
