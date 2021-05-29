from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=200, default='')
    img = models.ImageField()

    def __str__(self):
        return self.title
