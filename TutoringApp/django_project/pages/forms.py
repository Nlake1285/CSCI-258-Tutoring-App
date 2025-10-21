from django import forms
from django.core.exceptions import ValidationError

from .models import TutoringHour


class TutoringHourForm(forms.ModelForm):
    class Meta:
        model = TutoringHour
        fields = ['day_of_week', 'start_time', 'end_time', 'location']
        widgets = {
            'start_time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control',
                    'help_text': 'Enter time in 24-hour format (e.g., 08:00 for 8 AM, 16:00 for 4 PM)'
                }
            ),
            'end_time': forms.TimeInput(
                attrs={
                    'type': 'time', 
                    'class': 'form-control',
                    'help_text': 'Enter time in 24-hour format (e.g., 09:00 for 9 AM, 17:00 for 5 PM)'
                }
            ),
            'day_of_week': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CS Fishbowl'}),
        }
        help_texts = {
            'start_time': 'Use 24-hour format: 08:00 for 8 AM, 16:00 for 4 PM',
            'end_time': 'Use 24-hour format: 09:00 for 9 AM, 17:00 for 5 PM',
        }
    
    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        
        if start_time and end_time:
            if start_time >= end_time:
                raise ValidationError("End time must be after start time.")
        
        return cleaned_data