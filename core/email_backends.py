# core/email_backends.py
from django.core.mail.backends.base import BaseEmailBackend
from django.conf import settings
from sib_api_v3_sdk import Configuration, ApiClient
from sib_api_v3_sdk.api import TransactionalEmailsApi
from sib_api_v3_sdk.models import SendSmtpEmail

class BrevoEmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        configuration = Configuration()
        configuration.api_key['api-key'] = settings.BREVO_API_KEY

        api_instance = TransactionalEmailsApi(ApiClient(configuration))
        sent_count = 0

        for message in email_messages:
            try:
                html_content = None
                if hasattr(message, 'alternatives'):
                    for alt in message.alternatives:
                        if alt[1] == 'text/html':
                            html_content = alt[0]
                            break

                # Parse le nom et email depuis from_email
                from_name, from_email = self.parse_from_email(message.from_email)

                send_email = SendSmtpEmail(
                    subject=message.subject,
                    html_content=html_content or message.body,
                    text_content=message.body,
                    sender={"name": from_name, "email": from_email},
                    to=[{"email": addr} for addr in message.to],
                )
                api_instance.send_transac_email(send_email)
                sent_count += 1

            except Exception as e:
                if not self.fail_silently:
                    raise e

        return sent_count

    def parse_from_email(self, from_email):
        """
        Gère le format 'Nom <email@ex.com>' ou simplement 'email@ex.com'
        """
        if '<' in from_email and '>' in from_email:
            name = from_email.split('<')[0].strip()
            email = from_email.split('<')[1].replace('>', '').strip()
        else:
            name = email = from_email.strip()
        return name, email
