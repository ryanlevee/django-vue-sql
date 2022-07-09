from django.forms import ModelForm, Textarea, EmailInput, TextInput

from .models import ContactUs


class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = ['email', 'subject', 'message']
        widgets = {
            'email': EmailInput(
                attrs={'autofocus': True, 'class': 'form-control'}
            ),
            'subject': TextInput(
                attrs={'class': 'form-control'}
            ),
            'message': Textarea(
                attrs={'rows': 10, 'class': 'form-control'}
            )
        }
