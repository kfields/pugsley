from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as UserManagerBase

from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class UserManager(UserManagerBase):
    pass

class User(AbstractUser):
    objects = UserManager()

class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = User.objects.get(email=sociallogin.email_addresses[0])
        sociallogin.connect(request, user)
