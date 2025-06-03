# core/views.py

from django.http import HttpResponse
from core.utils.email import send_email_via_brevo

def test_email(request):
    to = "themrx66@gmail.com"
    subject = "akhir test email"
    html_content = "<h1>This is a test</h1>"
    response = send_email_via_brevo(to, subject, html_content)
    return HttpResponse(f"Email sent: {response}")

def home(request):
    return HttpResponse("Bienvenue sur Portfolio AI 👋")