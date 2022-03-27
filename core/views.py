from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    if request.user.is_authenticated:
        return redirect(reverse("decisions:index"))
    return redirect(reverse("users:login"))

    
class ProtectedView(LoginRequiredMixin):
    login_url = "/users/login/"