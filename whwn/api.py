from tastypie.resources import ModelResource
from whwn.models import (Item, SKU, Category, Message, Team, User)
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from tastypie.authorization import Authorization
from tastypie.authentication import (MultiAuthentication, ApiKeyAuthentication,
                                    SessionAuthentication)
from tastypie import fields
from tastypie.utils import trailing_slash
from django.conf.urls import url
from django.http import HttpResponse

class ItemResource(ModelResource):
    class Meta:
        queryset = Item.objects.all()
        resource_name = 'item'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication, ApiKeyAuthentication)

class SKUResource(ModelResource):
    class Meta:
        queryset = SKU.objects.all()
        resource_name = 'sku'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication, ApiKeyAuthentication)

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication, ApiKeyAuthentication)

class MessageResource(ModelResource):
    class Meta:
        queryset = Message.objects.all()
        resource_name = 'message'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication, ApiKeyAuthentication)

class TeamResource(ModelResource):
    class Meta:
        queryset = Team.objects.all()
        resource_name = 'team'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication, ApiKeyAuthentication)

class UserResource(ModelResource):

    raw_password = fields.CharField(attribute=None, readonly=True, null=True,
            blank=True)

    class Meta:
        always_return_data = True
        authorization = Authorization()
        queryset = User.objects.all()
        resource_name = 'user'
        detail_uri_name = 'username'
        allowed_methods = ['get', 'post']

    def prepend_urls(self):
        '''
        We need additional `sign in` and `sign out` routes for our Backbone
        web app to consume.
        '''
        return [
            # Signin and signout resources
            url(r"^(?P<resource_name>%s)/signin%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('signin'), name="user_signin"),
            url(r"^(?P<resource_name>%s)/signout%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('signout'), name="user_signout"),
            # This along with `detail_uri_name` forces the 'get' call on
            # to use the user.username instead of user.id. This makes
            # frontend calls easier since usernames are guaranteed unique,
            # and are more readily exposed than user ids.
            url(r"^(?P<resource_name>%s)/(?P<username>[\w\d_.-]+)%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view("dispatch_detail"), name="api_dispatch_detail"),
        ]

    def hydrate(self, bundle):
        '''
        Custom hydrate to get user creation to work. In this case
        user creation needs to do `make_password` on the raw password
        passed in form the create user form.
        '''
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

    def signin(self, request, **kwargs):
        '''
        Sign in a user given a username and password.
        Expects json in request.body
        '''
        self.method_check(request, allowed=['post'])

        import json
        data = json.loads(request.body)

        u = authenticate(username=data.get('username'),
                         password=data.get('raw_password'))
        if u and u.is_active:
            login(request, u)
            kwargs = {'pk': u.id, 'api_name': u'v1', 'resource_name': u'user'}
            return self.get_detail(request, **kwargs)
        else:
            return HttpResponse(status=401)

    def signout(self, request, **kwargs):
        '''
        Logout a user by grabbing the user id out of the
        session if the session is a valid session.
        '''
        self.method_check(request, allowed=['post'])

        try:
            session = Session.objects.get(session_key=request.COOKIES.get('sessionid'))
            uid = session.get_decoded().get('_auth_user_id')
            user = User.objects.get(pk=uid)
            if user:
                logout(request)
                return HttpResponse(status=200)
        except Session.DoesNotExist:
            pass
        return HttpResponse(status=401)

