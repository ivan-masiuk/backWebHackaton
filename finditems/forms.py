from django import forms
from finditems.models import *


class CreateItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'img', 'desc']
