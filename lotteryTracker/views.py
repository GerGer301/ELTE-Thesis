
# from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account.views import PasswordChangeView, PasswordResetView
from django.urls import reverse_lazy


class MyPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('dashboards:dashboard')

