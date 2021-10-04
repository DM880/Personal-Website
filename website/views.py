from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import HttpResponse
from .models import *
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

# Create your views here.

def index(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')

        try:
            validate_email(email)
        except ValidationError as error_email:
            print("bad email, details:", error_email)
        else:
            ContactDetail.objects.create(name=name,email=email,text=text)

            # subject = "Thank you for reaching out!"

            # body = {
            #     'name':name,
            #     'email':email,
            #     'text':text
            # }

            # message = "Thank you for reaching out!I will do my best to get in contact with you as soon as possible"

            # try:
            #     send_mail(subject, message, "my@email.com", [email])
            # except BadHeaderError:
            #     return HttpResponse("Not valid")

            message = Mail(
                from_email= settings.EMAIL_HOST,
                to_emails=email,
                subject='Thank you for reaching out!',
                html_content='<strong>Thank you for reaching out!I will do my best to get in contact with you as soon as possible</strong>')
            try:
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e.message)

            return redirect('website:index')

    return render(request, "index.html")


def comingsoon(request):
    return render(request, "comingsoon.html")