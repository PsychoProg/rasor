from django.db import models
from django.contrib.auth.models import User 

class Profile(models.Model):
    pass 


class Otp(models.Model):
    token = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=254)
    pass_code = models.SmallIntegerField()
    expiration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email