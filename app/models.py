from django.db import models


class Group(models.Model):
    class Meta:
        verbose_name = 'Група'
        verbose_name_plural = 'Групи'

    name = models.CharField(max_length=20, default='group-name')

    def __str__(self):
        return self.name


class Week(models.Model):
    class Meta:
        verbose_name = 'Тиждень'
        verbose_name_plural = 'Тиждні'

    name = models.CharField(max_length=100, default='week-name')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, related_name='weeks')

    def __str__(self):
        return f'{self.name} - {self.group.name}'


class Tutor(models.Model):
    class Meta:
        verbose_name = 'Викладач'
        verbose_name_plural = 'Викладачі'

    first_name = models.CharField(max_length=200, default='fist-name')
    last_name = models.CharField(max_length=200, default='last-name')
    img = models.ImageField(blank=True)
    link_zoom = models.URLField(default='')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Lesson(models.Model):
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предмети'

    name = models.CharField(max_length=200)
    tutors = models.ManyToManyField(Tutor)

    def __str__(self):
        return self.name


class Day(models.Model):
    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дні'

    name = models.CharField(max_length=50, default='day-name')
    week = models.ForeignKey(Week, on_delete=models.CASCADE, null=True, related_name='days')

    lesson_1 = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True, related_name='lesson1')
    tutor_1 = models.ForeignKey(Tutor, on_delete=models.CASCADE, null=True, blank=True, related_name='tutor_1')

    lesson_2 = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True, related_name='lesson2')
    tutor_2 = models.ForeignKey(Tutor, on_delete=models.CASCADE, null=True, blank=True, related_name='tutor_2')

    lesson_3 = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True, related_name='lesson3')
    tutor_3 = models.ForeignKey(Tutor, on_delete=models.CASCADE, null=True, blank=True, related_name='tutor_3')

    lesson_4 = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True, related_name='lesson4')
    tutor_4 = models.ForeignKey(Tutor, on_delete=models.CASCADE, null=True, blank=True, related_name='tutor_4')

    lesson_5 = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True, related_name='lesson5')
    tutor_5 = models.ForeignKey(Tutor, on_delete=models.CASCADE, null=True, blank=True, related_name='tutor_5')

    def __str__(self):
        return f'{self.name} - {self.week.group.name}'
