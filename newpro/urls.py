
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
    url(r'^sczone/',include(('sczone.scurl','sczone'),namespace="sczone")),
url(r'^adminzone/',include(('adminzone.adminzoneurls','adminzone'),namespace='adminzone')),



]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
