from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from tastypie.api import Api
from whwn.api import (ItemResource, SKUResource, CategoryResource,
                        MessageResource, TeamResource, UserResource)


v1_api = Api(api_name='v1')
v1_api.register(ItemResource())
v1_api.register(SKUResource())
v1_api.register(CategoryResource())
v1_api.register(MessageResource())
v1_api.register(TeamResource())
v1_api.register(UserResource())

urlpatterns = patterns('whwn.views',
    url(r'^api/', include(v1_api.urls)),
    url(r'^', TemplateView.as_view(template_name="index.html")),
)
