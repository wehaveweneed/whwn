from django.conf.urls import patterns, include, url
from tastypie.api import Api
from whwn.api import (ItemResource, SKUResource, CategoryResource,
                        MessageResource, TeamResource, UserResource)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


v1_api = Api(api_name='v1')
v1_api.register(ItemResource())
v1_api.register(SKUResource())
v1_api.register(CategoryResource())
v1_api.register(MessageResource())
v1_api.register(TeamResource())
v1_api.register(UserResource())

urlpatterns = patterns('',

    (r'^api/', include(v1_api.urls)),
    # Examples:
    # url(r'^$', 'whwn.views.home', name='home'),
    # url(r'^whwn/', include('whwn.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
