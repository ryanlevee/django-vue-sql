from django.forms import ModelForm, Textarea
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'message']
        widgets = {
          'message': Textarea(
            attrs={'autofocus': True, 'rows': 10}
          )
        }
