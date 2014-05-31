# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponseRedirect
from django.views.generic import View
from custom.common_functions import get_json_response
from custom.custom_mixin import CommonViewMixin, LoginMixin
from file_upload.forms import FileUploadForm
from file_upload.models import FileUpload


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/signin/')

class Signup(View,CommonViewMixin):
    template_name = "signup.html"

    def get_persistent_context(self, request, *args, **kwargs):
        return kwargs

    def get_context(self, request, *args, **kwargs):
        return {}

    #@transaction.atomic()
    def ajax_post(self,request,*args,**kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email_id = request.POST.get('email')
        username= request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        try:
            if password != confirm_password:
                return get_json_response({'status':200,'alert_message':"Passwords should match"})
            else:
                user = User.objects.create(username=username, first_name=first_name, last_name=last_name, email = email_id)
                user.set_password(password)
                user.save()
                return get_json_response({'status':200,'alert_message':"You have successfully registered yourself on our site!!"})
        except Exception as e:
            raise Exception

class Login(View,CommonViewMixin,LoginMixin):
    template_name = 'singin.html'

    def get_persistent_context(self, request, *args, **kwargs):
        return kwargs

    def post(self, request, *args, **kwargs):
        logged_in, msg = self.logger(request)
        if logged_in:
            #is_valid = self.validate_user(request, *args, **kwargs)
            return HttpResponseRedirect('/upload-file/')
        else:
            return HttpResponseRedirect(request.path)

class FileUploadView(View,CommonViewMixin,LoginMixin):
    template_name = 'handle_files.html'

    def get_persistent_context(self, request, *args, **kwargs):
        return kwargs

    def get_context(self, request, *args, **kwargs):
        if not request.session.get('form_saved'):
            file_form = FileUploadForm()
            all_files = FileUpload.objects.filter(user=request.user)
            return {'file_form':file_form, 'all_files':all_files}
        else:
            del request.session['form_saved']
            return {'form_saved': True}

    def non_ajax_post(self, request, *args, **kwargs):
        file_form = FileUploadForm(request.POST,request.FILES)
        if file_form.is_valid():
            try:
                file_upload = file_form.save(commit=False)
                file_upload.user = request.user
                file_obj = request.FILES.get('file')
                file_name = file_obj.name
                file_upload.name = file_name
                file_upload.save()
                request.session['form_saved'] = True
            except Exception as e:
                print e.message
            return HttpResponseRedirect(request.path)
        else:
            return HttpResponseRedirect(request.path)


