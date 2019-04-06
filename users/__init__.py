from .models import CustomUser
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        # This isn't tested, but should work
        try:
            user = CustomUser.objects.get(email=sociallogin.email)
            sociallogin.connect(request, user)
            # Create a response object
            raise ImmediateHttpResponse(response)
        except User.DoesNotExist:
            pass
