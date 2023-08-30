from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User 


class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if "@" in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}

        try:
            user = User.objects.get(**kwargs)
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user

    def get_user(self, username):
        try:
            return User.objects.get(pk=username)
        except User.DoesNotExist:
            return None
