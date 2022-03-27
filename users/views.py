from django.views import View
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import UserRegisterForm


class LoginView(LoginView):
    template_name = "users/login.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse("decisions:index"))
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return "/"


class LogoutView(LogoutView):
    template_name = "users/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AuthenticationForm()
        context["logout_message"] = "You have been logged out"
        return context
    
    
class RegisterView(View):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse("decisions:index"))
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("decisions:index"))
        return render(request, self.template_name, {'form': form})
