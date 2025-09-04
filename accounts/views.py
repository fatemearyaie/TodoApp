from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.http import HttpResponse

# Create your views here.
class LoginView(LoginView):
    template_name = 'registeration/login.html'
    fields = "username", "password"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task_list')

def task_list(request):
    return HttpResponse('hiiiiiii')


class RegisterView(FormView):
    """
    it shows which template this view is related, which form class is related and what should we do after the success
    """
    template_name = 'registeration/register.html'
    form_class = UserCreationForm
    redirect_authenticate_user = True
    success_url = reverse_lazy('task_list')
    """
    get a form, save it. if the form is not none login the user.
    """
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('login')
        return super(RegisterView, self).get(*args, **kwargs)



