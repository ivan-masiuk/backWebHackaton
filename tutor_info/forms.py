from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class StudentVoteForm(forms.Form):
    punctuality = forms.IntegerField(label="Пунктуальність", validators=[
                                                    MinValueValidator(1),
                                                    MaxValueValidator(10)])
    loyalty = forms.IntegerField(label="Лояльність", validators=[
                                                    MinValueValidator(1),
                                                    MaxValueValidator(10)])
    grading = forms.IntegerField(label="Система оцінювання", validators=[
                                                    MinValueValidator(1),
                                                    MaxValueValidator(10)])

    class Meta:
        fields = ('punctuality', 'loyalty', 'grading')
