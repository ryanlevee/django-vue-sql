from datetime import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm


BIRTH_YEAR_CHOICES = range(1915, datetime.now().year)

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name',
                  'last_name', 'dob', 'avatar')
        widgets = {
            'dob': forms.SelectDateWidget(
                attrs={
                    'style': 'width: 25.85%; display: inline; margin: 0 1%'
                },
                years = BIRTH_YEAR_CHOICES
            ),
        }
