from django.forms import ModelForm, Textarea, NullBooleanSelect
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['game_title', 'message']
        widgets = {
          'message': Textarea(
            attrs={'autofocus': True, 'rows': 10}
          ),
        }
