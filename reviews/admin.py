from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from common.admin import DjangoGamesAdmin

from .models import Review


@admin.register(Review)
class ReviewAdmin(DjangoGamesAdmin):
    model = Review
    list_display = ['message', 'user', 'game_title', 'id']
    list_filter = ['game_title', 'user']
    ordering = ['user']

    formfield_overrides = {
      models.CharField: {'widget': TextInput(attrs={'size':'50'})},
      models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
      }
