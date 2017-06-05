from django import forms
from Database.models import Entry
from splitjson.widgets import SplitJSONWidget
from django.forms import ModelForm

from Linguistics.models import LinguisticQuestion, LinguisticRule




class linguisticsRForm(forms.ModelForm):

    class Meta:
        model = LinguisticRule
        fields = (
            'name',
            'description',
            'word',
            'gr',
            'ph',
            'CVC'
        )




class linguisticsQForm(forms.ModelForm):

    class Meta:
        model = LinguisticQuestion
        fields = (
            'name',
            'question',
        )


