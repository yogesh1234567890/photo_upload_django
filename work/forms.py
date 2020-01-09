from django import forms
from work.models import Work

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields=['name','email','image']