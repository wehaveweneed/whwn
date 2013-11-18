from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.conf import settings

class SignInView(FormView):
    """
    This class gives us a JSON endpoint to login a user.
    """

    form_class=AuthenticationForm

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(SignInView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        #TODO: return a response to login user
        return True

    def form_invalid(self, form):
        #TODO: return error response and render notifications
        return False

    def post(self, request, *args, **kwargs):
    
