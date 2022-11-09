from django.forms import ModelForm, Textarea, EmailInput, TextInput

from .models import ContactUs


class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = ['first_name', 'last_name', 'email', 'subject', 'message']
        widgets = {
            'first_name': TextInput(
                attrs={'autofocus': True, 'class': 'form-control'}
            ),
            'last_name': TextInput(
                attrs={'class': 'form-control'}
            ),
            'email': EmailInput(
                attrs={'class': 'form-control'}
            ),
            'subject': TextInput(
                attrs={'class': 'form-control'}
            ),
            'message': Textarea(
                attrs={'rows': 10, 'class': 'form-control'}
            )
        }
