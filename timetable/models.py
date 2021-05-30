from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from account.models import Profile


class Group(models.Model):
    title = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'Група'
        verbose_name_plural = 'Групи'

    def __str__(self):
        return self.title


class Subject(models.Model):
    title = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предмети'

    def __str__(self):
        return self.title


class Pair(models.Model):
    subject_fk = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='pairs')
    tutor_fk = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='pairs')
    week_day_fk = models.ForeignKey('DayOfTheWeek', on_delete=models.CASCADE, related_name='pairs')
    place = models.TextField(max_length=200)
    position = models.PositiveIntegerField(default=1, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)])

    class Meta:
        verbose_name = 'Пара'
        verbose_name_plural = 'Пари'

    def __str__(self):
        return f'{self.subject_fk.title}-{self.week_day_fk.name_weekday}'


class DayOfTheWeek(models.Model):
    NAME_CHOICES = (
        ('Понеділок', 'Понеділок'),
        ('Вівторок', 'Вівторок'),
        ('Середа', 'Середа'),
        ('Четвер', 'Четвер'),
        ("П'ятниця", "П'ятниця"),
        ('Субота', 'Субота'),
        ('Неділя', 'Неділя'),
    )
    week_fk = models.ForeignKey('Week', on_delete=models.CASCADE, related_name='week_days')

    name_weekday = models.CharField(max_length=15, choices=NAME_CHOICES)

    def __str__(self):
        return f'{self.name_weekday}-{self.week_fk.type_week}'

    class Meta:
        verbose_name = 'День тижня'
        verbose_name_plural = 'Дні тижня'


class Week(models.Model):
    TYPE_WEEK = (
        ('red', 'Червона'),
        ('blue', 'Синя')
    )
    group_fk = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='weeks')

    type_week = models.CharField(max_length=15, choices=TYPE_WEEK)

    class Meta:
        verbose_name = 'Тиждень'
        verbose_name_plural = 'Тижні'

    def __str__(self):
        return f'{self.type_week}'
