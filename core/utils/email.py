import os
from sib_api_v3_sdk import Configuration, ApiClient
from sib_api_v3_sdk.api.transactional_emails_api import TransactionalEmailsApi
from sib_api_v3_sdk.models import SendSmtpEmail

def send_email_via_brevo(to, subject, html_content):
    configuration = Configuration()
    configuration.api_key['api-key'] = os.getenv("BREVO_API_KEY")

    api_client = ApiClient(configuration)
    api_instance = TransactionalEmailsApi(api_client)

    send_smtp_email = SendSmtpEmail(
        to=[{"email": to}],
        sender={"name": "Portfolio AI", "email": "themrx.test9@gmail.com"},
        subject=subject,
        html_content=html_content,
    )

    try:
        response = api_instance.send_transac_email(send_smtp_email)
        return response
    except Exception as e:
        print(f"Erreur d'envoi: {e}")
        return None
