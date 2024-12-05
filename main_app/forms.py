from django import forms
from .models import Rating, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['date', 'comment']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['date', 'rating']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }
