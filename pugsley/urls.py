import socket

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^pages/', include(wagtail_urls)),

    path('myaccount/', include('myaccount.urls')),
    path('myaccount/', include('django.contrib.auth.urls')),
    path('myaccount/', include('allauth.urls')),
    
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    
    path('', include('blog.urls')),
    path('avatar/', include('avatar.urls')),
    path('schedule/', include('schedule.urls')),
    path('graphql/', include('gql.urls')),

    path('token-auth/', obtain_jwt_token),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
