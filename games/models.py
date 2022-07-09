import datetime
from django.conf import settings
from django.db import models

now = datetime.datetime.now()
mow = now.strftime("%Y-%m-%d %H:%M:%S")


class ContactUs(models.Model):
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return f'{self.email, self.subject, self.message, self.timestamp}'


class Title(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name='title',
        default=1
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Titles'
        ordering = ['title']


class Game(models.Model):
    title = models.TextField()
    score = models.SmallIntegerField()
    operation = models.CharField(max_length=3, blank=True)
    max_number = models.SmallIntegerField(blank=True)
    word_length = models.SmallIntegerField(blank=True)
    timestamp = models.DateTimeField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name='games',
        default=1
    )

    game_title = models.ForeignKey(
        Title, on_delete=models.CASCADE,
        related_name='games'
    )

    def __str__(self):
        return f'''{self.title, self.score, self.operation,
                    self.max_number, self.word_length, self.timestamp}'''

    class Meta:
        verbose_name_plural = 'Leaderboard'
