from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

User._meta.get_field('email')._unique = True


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

    third_name = models.CharField(max_length=20, default='ThirdName')
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    img = models.ImageField(blank=True)

    def __str__(self):
        return f'ID Profile:{self.id}'
