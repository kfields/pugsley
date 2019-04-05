from django.contrib.auth.models import AbstractUser, UserManager
from allauth.account.models import EmailAccount
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        # This isn't tested, but should work
        try:
            user = User.objects.get(email=sociallogin.email)
            sociallogin.connect(request, user)
            # Create a response object
            raise ImmediateHttpResponse(response)
        except User.DoesNotExist:
            pass

class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()