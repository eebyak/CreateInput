from django import forms
from Database.models import Entry
from splitjson.widgets import SplitJSONWidget
from django.forms import ModelForm

from Wordout.models import AssociationTable
from Games.models import Game, GameType
from Linguistics.models import LinguisticRule

class associateForm(forms.ModelForm):

    class Meta:
        model = AssociationTable
        fields = (
            'name',
            'question',
            # 'gameType',
            # 'linguistic_rule_input',
            # 'linguistic_rule_output'
        )


class rulesForm(forms.Form):
    rules = forms.ModelChoiceField(queryset=LinguisticRule.objects.all().order_by('name'))


