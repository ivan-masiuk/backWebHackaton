from django.db import models
from account.models import Profile


class Item(models.Model):
    title = models.CharField(max_length=200, default='')
    img = models.ImageField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
