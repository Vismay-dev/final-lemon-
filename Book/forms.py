from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
        widget = {
            'title' : forms.TextInput(attrs={
                'class' : 'form-controll'
            }),
            'author' : forms.Select(attrs={
               'class' : 'form-controll' 
            })
        }
        
        labels = {
            'title' : " Book Title ",
            'author' : " Author Name ",
        }
        
        def clean_title(self):
            title = self.cleaned_data.get('title')
            if not title[0].isupper():
                raise forms.ValidationError('Title Must Start with a Capital Letter!')
            return title