from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class StudentVoteForm(forms.Form):
    punctuality = forms.IntegerField(label="Пунктуальність", validators=[
                                                    MinValueValidator(1),
                                                    MaxValueValidator(5)])
    loyalty = forms.IntegerField(label="Лояльність", validators=[
                                                    MinValueValidator(1),
                                                    MaxValueValidator(5)])
    grading = forms.IntegerField(label="Система оцінювання", validators=[
                                                    MinValueValidator(1),
                                                    MaxValueValidator(5)])
    relevance = forms.IntegerField(label="Актуальність матеріалу", validators=[
                                                    MinValueValidator(1),
                                                    MaxValueValidator(5)])

    positive = forms.IntegerField(label="Позитивний настрій", validators=[
        MinValueValidator(1),
        MaxValueValidator(5)])

    class Meta:
        fields = ('punctuality', 'loyalty', 'grading', 'relevance', 'positive')
