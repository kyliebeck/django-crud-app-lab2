from django import forms
from .models import Expense

class DateForm(forms.ModelForm):
    class Meta:
        model = Expense
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            )
        }