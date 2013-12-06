from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.template.response import TemplateResponse
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'', include('whwn.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^404/$', TemplateResponse, {'template': '404.html'}))

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
