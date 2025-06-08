import os
from django.core.mail.backends.base import BaseEmailBackend
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

class BrevoEmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        api_key = os.getenv('BREVO_API_KEY')
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = api_key
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
        sent_count = 0
        for message in email_messages:
            to_emails = []
            for addr in message.to:
                if isinstance(addr, tuple):
                    to_emails.append({"email": addr[1], "name": addr[0]})
                else:
                    to_emails.append({"email": addr})
            # Use a valid sender email (must be validated in Brevo)
            sender_email = os.getenv('DEFAULT_FROM_EMAIL', 'themrx.test9@gmail.com')
            if '<' in sender_email and '>' in sender_email:
                # Extract email from format: Name <email@domain.com>
                import re
                match = re.search(r'<(.+?)>', sender_email)
                sender_email = match.group(1) if match else sender_email
            sender = {"email": sender_email, "name": sender_email.split('@')[0]}
            email = sib_api_v3_sdk.SendSmtpEmail(
                to=to_emails,
                subject=message.subject,
                html_content=message.body,
                sender=sender,
            )
            try:
                api_instance.send_transac_email(email)
                sent_count += 1
            except ApiException as e:
                if not self.fail_silently:
                    raise
        return sent_count
