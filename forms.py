from django import forms
from . import models

class MenuForm(forms.ModelForm):
    
    class Meta:
        model = models.MenuItem
        fields = '__all__'