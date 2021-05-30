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


class TutorStatistic(VoteAbstract):
    tutor_profile_fk = models.ForeignKey('account.Profile', on_delete=models.CASCADE, related_name='statistics')

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
