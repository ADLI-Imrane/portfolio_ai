from allauth.account.adapter import DefaultAccountAdapter
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

class CustomAccountAdapter(DefaultAccountAdapter):
    def send_confirmation_mail(self, request, emailconfirmation, signup):
        activate_url = self.get_email_confirmation_url(request, emailconfirmation)
        ctx = {
            "user": emailconfirmation.email_address.user,
            "activate_url": activate_url,
            "current_site": request.get_host(),
            "email": emailconfirmation.email_address.email,
        }

        subject = "Confirmez votre adresse email"
        from_email = None  # utilisera DEFAULT_FROM_EMAIL

        # HTML + TXT email
        text_body = render_to_string("account/email/email_confirmation_message.txt", ctx)
        html_body = render_to_string("account/email/email_confirmation_message.html", ctx)

        msg = EmailMultiAlternatives(subject, text_body, from_email, [emailconfirmation.email_address.email])
        msg.attach_alternative(html_body, "text/html")
        msg.send()
