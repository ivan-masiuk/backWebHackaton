from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

User._meta.get_field('email')._unique = True


class AbstractUser(models.Model):
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    TYPE_USER_CHOICES = (
        ('tutor', 'Викладач'),
        ('student', 'Студент'),
    )
    type_user = models.CharField(max_length=15, choices=TYPE_USER_CHOICES)

    class Meta:
        abstract = True


class Tutor(AbstractUser):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)


class Student(AbstractUser):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
