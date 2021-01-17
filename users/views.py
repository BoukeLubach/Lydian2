from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic import View, ListView, DetailView



def home(request):

    return render(request, 'home.html', context = {})

class LoginView(LoginView):
    template_name = 'users/login.html'

class LogoutView(LogoutView):
    template_name = 'users/logout.html'

class MyPasswordChangeView(PasswordChangeView):
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('password-change-done')


    link_classes = {
        'password' : 'active',
    }

    extra_context = {
        'link_class': link_classes,
    }

    def get_context_data(self, **kwargs):
        context = super(MyPasswordChangeView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


    def get_context_data(self, **kwargs):
        context = super(MyPasswordResetDoneView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context



@login_required
def profile(request):
    selected_profile = Profile.objects.get(id=request.user.id)
    selected_user = selected_profile.user

    link_classes = {
        'profile': 'active',
    }


    context = {
        'profile': selected_profile,
        'link_class': link_classes,
    }

    return render(request, 'users/profile.html', context=context)


@login_required
def account_view(request):

    link_classes = {
        'account': 'active',
    }

    context = {
        'link_class': link_classes,
    }

    return render(request, 'users/profile_account_view.html', context=context)


class AccountUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ['email']

    link_classes = {
        'account' : 'active',
    }
    extra_context = {
        'link_class': link_classes,
    }

    def get_context_data(self, **kwargs):
        context = super(AccountUpdateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy("profile")