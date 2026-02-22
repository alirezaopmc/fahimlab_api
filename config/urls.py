"""
URL configuration for config project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

from config.api import api_router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v2/", api_router.urls),
    path("cms/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("pages/", include(wagtail_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
