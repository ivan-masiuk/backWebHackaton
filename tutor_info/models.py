from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class VoteAbstract(models.Model):
    punctuality = models.PositiveIntegerField(default=1, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)])
    loyalty = models.PositiveIntegerField(default=1, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)])
    grading = models.PositiveIntegerField(default=1, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)])
    relevance = models.PositiveIntegerField(default=1, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)])
    positive = models.PositiveIntegerField(default=1, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)])

    class Meta:
        abstract = True


class TutorStatistic(models.Model):
    tutor_profile_fk = models.ForeignKey('account.Profile', on_delete=models.CASCADE, related_name='statistics')

    punctuality = models.FloatField(default=0.0)
    loyalty = models.FloatField(default=0.0)
    grading = models.FloatField(default=0.0)
    relevance = models.FloatField(default=0.0)
    positive = models.FloatField(default=0.0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Статистика викладача'
        verbose_name_plural = 'Статистики викладачів'


class VoteStudent(VoteAbstract):
    tutor_profile_fk = models.ForeignKey('account.Profile', on_delete=models.CASCADE, related_name='votes_by_student')
    student_profile_fk = models.ForeignKey('account.Profile', on_delete=models.CASCADE, related_name='votes_for_tutor')

    class Meta:
        verbose_name = 'Голос студента'
        verbose_name_plural = 'Голоси студентів'
