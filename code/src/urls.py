from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


# SWAGGER CONFIGURATIONS
schema_view = get_schema_view(
   openapi.Info(
      title="Fitness API",
      default_version='v1',
      contact=openapi.Contact(email="test@task.local"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # login and logout using DRF
    path('api-auth/', include('rest_framework.urls')),

    # swagger paths
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # THIS PATH FOR APIs
    path('api/', include('src.api_urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
