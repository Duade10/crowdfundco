from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import default_token_generator

# Account Verification Imports
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode


class User(AbstractUser):
    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_FACEBOOK = "facebook"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_FACEBOOK, "Facebook"),
        (LOGIN_GITHUB, "Github"),
    )

    phone_number = models.CharField(max_length=20, null=True)
    login_method = models.CharField(max_length=20, choices=LOGIN_CHOICES, null=True, blank=True)
    facebook_profile = models.URLField(blank=True)
    twitter_profile = models.URLField(blank=True)
    linkedin_profile = models.URLField(blank=True)
    receive_notifications = models.BooleanField(default=True)
    user_type = models.CharField(
        max_length=50, choices=[("Investor", "Investor"), ("Organizer", "Organizer"), ("Contributor", "Contributor")]
    )

    def save(self, *args, **kwargs):
        self.first_name = str.capitalize(self.first_name)
        self.last_name = str.capitalize(self.last_name)

        super().save(*args, **kwargs)

    def get_full_name(self) -> str:
        return super().get_full_name()

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

    # def verify_email(self, request):
    #     current_site = get_current_site(request)
    #     domain = current_site

    #     uid = urlsafe_base64_encode(force_bytes(self.pk))
    #     token = default_token_generator.make_token(self)

    #     html_message = render_to_string(
    #         "users/mail/user_verification_email.html",
    #         {"domain": domain, "uidb64": uid, "token": token, "first_name": self.first_name},
    #     )

    #     send_mail(
    #         "Activate your Account",
    #         strip_tags(html_message),
    #         settings.EMAIL_HOST_USER,
    #         [self.email],
    #         fail_silently=False,
    #         html_message=html_message,
    #     )

    #     self.save()

    # def send_reset_email(self, request):
    #     current_site = get_current_site(request)
    #     domain = current_site
    #     uid = urlsafe_base64_encode(force_bytes(self.pk))
    #     token = default_token_generator.make_token(self)

    #     html_message = render_to_string(
    #         "users/mail/reset_password_email.html",
    #         {"domain": domain, "uid": uid, "token": token, "first_name": self.first_name},
    #     )
    #     send_mail(
    #         "Reset Your Password",
    #         strip_tags(html_message),
    #         settings.EMAIL_HOST_USER,
    #         [self.email],
    #         fail_silently=False,
    #         html_message=html_message,
    #     )
