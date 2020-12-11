from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
import random

# Create your views here.
def smtp_view(request):
    if request.method=='GET':
        subject = 'send the mail'
        email_from = settings.EMAIL_HOST_USER
        # html_content = get_template('mail.html').render()
        recipient_list = ['kushwaharaj241@gmail.com']
        otp=random.randrange(1111,9999)
        message=f"your otp is {otp}"
        email = EmailMultiAlternatives(subject, message, email_from, recipient_list)
        # email.attach_alternative(html_content, "text/html")
        email.send()
        return HttpResponse({"status": True})

