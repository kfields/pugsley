from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

urlpatterns = [
    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^pages/', include(wagtail_urls)),

    path('myaccount/', include('myaccount.urls')),
    path('myaccount/', include('django.contrib.auth.urls')),
    path('myaccount/', include('allauth.urls')),
    
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('avatar/', include('avatar.urls')),

    re_path(r'', include(wagtail_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
