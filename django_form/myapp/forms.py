from django import forms
from .models import Snippet


class ContactForm(forms.Form ) :

    name = forms.CharField()
    email = forms.EmailField(label='E-Mail')
    Choice = forms.ChoiceField(choices=[('Female','female'),('Male','male'),('Other','other')])
    
    body = forms.CharField(widget=forms.Textarea)


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('name','body')