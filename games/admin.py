from django.contrib import admin
from common.admin import DjangoGamesAdmin

from .models import Game, ContactUs, Title


@admin.register(ContactUs)
class ContactUsAdmin(DjangoGamesAdmin):
    model = ContactUs
    list_display = ['subject', 'email', 'message', 'timestamp']
    list_filter = ['email', 'timestamp']
    ordering = ['-timestamp']


@admin.register(Title)
class TitleAdmin(DjangoGamesAdmin):
    model = Title
    list_display = ['title']
    list_filter = ['title']


@admin.register(Game)
class GameAdmin(DjangoGamesAdmin):
    model = Game

    date_hierarchy = 'timestamp'
    list_display = ['user', 'game_title', 'score',
                    'operation', 'max_number',
                    'word_length', 'timestamp']
    list_filter = ['game_title', 'timestamp', 'user']
    ordering = ['-score']
    search_fields = ['user__username', 'score',
                     'operation', 'max_number',
                     'word_length', 'timestamp', ]
