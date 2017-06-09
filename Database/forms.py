from django import forms
from Database.models import Entry
from django.forms import ModelForm

class entryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = (
            'word',
            'CVC',
            'gr',
            'ph',
            'HFW',
            'dictionary',
        )



# class AuthorForm(ModelForm):
#
#     class Meta:
#         model = Author
#
#         fields=['author_id','first_name','last_name','email','age']

# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(required=False)