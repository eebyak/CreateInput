from django import forms
from Database.models import Entry
from django.forms import ModelForm

from Linguistics.models import  LinguisticRule




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



