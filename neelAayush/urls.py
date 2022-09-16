from django.contrib import admin
from django.urls import path, include, re_path
from base import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    # path(r'*download/(?P<path>.*)$', serve,{'download_root':settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)