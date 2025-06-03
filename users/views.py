# users/views.py
from django.http import HttpResponse
from django.contrib.auth.views import PasswordResetView
from django.conf import settings


class CustomPasswordResetView(PasswordResetView):
    template_name = 'account/password/password_reset.html'
    email_template_name = 'account/password/password_reset_email.txt'
    html_email_template_name = 'account/password/password_reset_email.html'
    subject_template_name = 'account/password/password_reset_subject.txt'

    def get_email_context(self):
        context = super().get_email_context()
        context['domain'] = settings.DEFAULT_DOMAIN  # → localhost:8000
        context['protocol'] = settings.DEFAULT_PROTOCOL  # → http
        return context
