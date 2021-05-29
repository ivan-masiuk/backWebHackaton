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

    class Meta:
        abstract = True


class TutorStatistic(VoteAbstract):
    tutor_fk = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='statistic')


class VoteStudent(VoteAbstract):
    tutor_fk = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='votes_by_student')
    student_fk = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='votes_for_tutor')
