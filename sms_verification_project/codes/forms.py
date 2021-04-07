from django import forms
from .models import Code

class CodeForm(forms.ModelForm):
    number = forms.CharField(label='Code', help_text='Enter SMS verification number')
    class Meta:
        model = Code
        fields = ('number',)
        