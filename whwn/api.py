from tastypie.resources import ModelResource
from whwn.models import (Item, SKU, Category, Message, Team, User)
from django.contrib.auth.hashers import make_password
from tastypie.authorization import Authorization
from tastypie import fields

class ItemResource(ModelResource):
    class Meta:
        queryset = Item.objects.all()
        resource_name = 'item'

class SKUResource(ModelResource):
    class Meta:
        queryset = SKU.objects.all()
        resource_name = 'sku'

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'

class MessageResource(ModelResource):
    class Meta:
        queryset = Message.objects.all()
        resource_name = 'message'

class TeamResource(ModelResource):
    class Meta:
        queryset = Team.objects.all()
        resource_name = 'team'

class UserResource(ModelResource):

    raw_password = fields.CharField(attribute=None, readonly=True, null=True,
            blank=True)

    class Meta:
        always_return_data = True
        authorization = Authorization()
        queryset = User.objects.all()
        resource_name = 'user'

    def hydrate(self, bundle):
        raw_password = bundle.data["raw_password"]
        bundle.data["password"] = make_password(raw_password)
        return bundle

    def dehydrate(self, bundle):
        bundle.data["key"] = bundle.obj.api_key.key
        try:
            del bundle.data["raw_password"]
        except KeyError:
            pass
        return bundle
