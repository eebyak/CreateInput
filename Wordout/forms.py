from django import forms
from Database.models import Entry
from splitjson.widgets import SplitJSONWidget
from django.forms import ModelForm

from Games.models import Game, GameType
from Linguistics.models import LinguisticRule, LinguisticQuestion

class associateForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = (
            'name',
            'type',
        )






