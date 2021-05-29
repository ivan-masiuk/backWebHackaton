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
    img = models.ImageField(blank=True)

    class Meta:
        abstract = True


class Tutor(AbstractUser):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    img = models.ImageField(blank=True)
    link_zoom = models.URLField(default='')

    class Meta:
        verbose_name = 'Викладач'
        verbose_name_plural = 'Викладачі'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Student(AbstractUser):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенти'
