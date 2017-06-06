from django import forms
from Database.models import Entry
from django.forms import ModelForm

from Games.models import Game, GameType


class gameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = (
            'name',
            'type',
        )




class gametypeForm(forms.ModelForm):

    class Meta:
        model = GameType
        fields = (
            'name',
            'description',
        )



