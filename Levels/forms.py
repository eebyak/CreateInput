from django import forms
from Database.models import Entry
from django.forms import ModelForm

from Levels.models import  Level, CVCLevels, WordLevels, LetterLevels


class levelForm(forms.ModelForm):
    class Meta:
        model = Level
        fields = (
            'name',
            'level',
            # 'type',
            'list'
        )


class letterForm(forms.ModelForm):
    class Meta:
        model = LetterLevels
        fields = (
            'name',
            'level',
            'list'
        )

class CVCForm(forms.ModelForm):
    class Meta:
        model = CVCLevels
        fields = (
            'name',
            'level',
            'list'
        )


class wordForm(forms.ModelForm):

    class Meta:
        model = WordLevels
        fields = (
            'name',
            'level',
            'list'
        )



