from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateResponseMixin
from custom.common_functions import get_json_response


class CommonViewMixin(TemplateResponseMixin):
    authorization = ''

    def get(self, request, *args, **kwargs):
        self.pre_rendering(request)
        self.kwargs_from_url = kwargs

        if not request.GET.keys():
            return self.render_page(request, *args, **kwargs)
        else:
            if request.GET.get('template') == 'true':
                return self.render_page(request, *args, **kwargs)
            else:
                if not self.is_valid(request) or not self._authorized(request, *args, **kwargs):
                    logout(request)
                    return get_json_response({'status': 403, 'error_msg': 'Not logged in'})
                return self.non_template_get_requests(request, *args, **kwargs)

    def _authorized(self, request, *args, **kwargs):
        for auth_callables in self.authorization:
            if callable(auth_callables):
                if not auth_callables(request, *args, **kwargs):
                    return False
        return True

    def non_template_get_requests(self, request, *args, **kwargs):
        pass

    def pre_rendering(self, request):
        pass

    def is_valid(self, request):
        return True

    def get_context(self, request, *args, **kwargs):
        return {}

    def get_persistent_context(self, request, *args, **kwargs):
        return {}

    def post(self, request, *args, **kwargs):
        not_valid = False
        if not self.is_valid(request) or not self._authorized(request, *args, **kwargs):
            logout(request)
            not_valid = True
        if request.is_ajax():
            if not_valid:
                return get_json_response({'status': 403, 'error_msg': 'Not logged in'})
            return self.ajax_post(request, *args, **kwargs)
        else:
            if not_valid:
                return HttpResponseRedirect('/logout/')
            return self.non_ajax_post(request, *args, **kwargs)

    def ajax_post(self, request, *args, **kwargs):
        raise NotImplemented

    def non_ajax_post(self, request, *args, **kwargs):
        raise NotImplemented

    def render_page(self, request ,*args, **kwargs):
        if not self.is_valid(request) or not self._authorized(request, *args, **kwargs):
            return HttpResponseRedirect('/logout/')

        context = self.get_context(request, *args, **kwargs)
        context.update(self.get_persistent_context(request, *args, **kwargs))
        self.before_response(request)
        return self.render_to_response(context=context)

    def before_response(self, request):
        pass


class LoginMixin(object):
    def authenticate(self,username,password):
        user = authenticate(username=username,password=password)
        if user:
            return user,None
        else:
            return None, {'msg': 'Invalid credentials'}

    def logger(self, request):
            username = request.POST.get('username')
            password = request.POST.get('password')
            user,message = self.authenticate(username=username,password=password)
            if user is None:
                return False, message
            else:
                login(request, user)
                return True, {}
