from django import forms
from .models import Rating, Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['date', 'comment']
