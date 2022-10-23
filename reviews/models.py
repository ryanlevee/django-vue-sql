from django.db import models

from games.models import Title
from play2learn import settings


class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='reviews'
    )
    game_title = models.ForeignKey(
        Title, on_delete=models.CASCADE,
        related_name='reviews'
    )
    message = models.TextField(max_length=120)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                # fields=['user', 'game_title'], name='one_review_per_user_per_game_title',
                fields=['user', 'game_title'], name='one_review_per_user_per_game',
            )
        ]
