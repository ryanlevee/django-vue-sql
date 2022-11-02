from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError

from .models import Applicant


def validate_checked(value):
    if not value:
        raise ValidationError("Required.")


class JobApplicationForm(forms.ModelForm):

    confirmation = forms.BooleanField(
        label = 'I certify that the information I have provided is true.',
        validators=[validate_checked]
    )

    resume = forms.FileField(
        # attrs={'accept':'application/pdf'},
        # validators=[validate_checked]
        # widgets=forms.FileInput()
    )

    class Meta:
        model = Applicant
        fields = (
            'first_name', 'last_name', 'email', 'website', 'employment_type',
            'start_date', 'available_days', 'desired_hourly_wage',
            'cover_letter', 'resume', 'confirmation', 'job')
        widgets = {
            'first_name': forms.TextInput(attrs={'autofocus': True}),
            'website': forms.TextInput(
                attrs = {'placeholder':'https://www.example.com'}
            ),
            'desired_hourly_wage': forms.NumberInput(
                attrs = {'min':'10.00', 'max':'100.00', 'step':'.25'}
            ),
            'start_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'available_days': forms.CheckboxSelectMultiple(attrs={'is_hidden':True}, required=True),
            'cover_letter': forms.Textarea(attrs={'cols': '100', 'rows': '5'}
            ),
            # 'resume': forms.FileInput(attrs={'accept':'application/pdf'}
            # ),
        }
        error_messages = {
            'start_date': {
                'past_date': 'Please enter a future date.'
            }
        }
