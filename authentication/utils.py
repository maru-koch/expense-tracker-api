from django.core.mail import send_mail, EmailMessage
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from .models import User
from django.urls import reverse



class Util:

    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data.get('subject'), 
            body=data.get('body'), 
            to =[data.get('email')]
            ) 
        email.send()

    @staticmethod
    def get_data_send_email(user_data, request):
        #: get user
        user = User.objects.get(email = user_data['email'])
        #: generate token
        token = RefreshToken.for_user(user).access_token
        #: get domain of the site
        current_site = get_current_site(request).domain

        #: the path associated with the named url in the reverse
        relative_link = reverse('email-verify')

        #: generate absolute url
        #: where the user will be taken to after clicking link
        abs_url = 'http://' + current_site + relative_link + '?token=' + str(token)

        #: email content
        subject = "verify your email"
        email_body = f"hi {user.username}, \nClick the link below to activate your account: \n"+abs_url
        data = {'subject':subject, 'email_body':email_body, 'email': user_data['email']}

        Util.send_email(data)

    