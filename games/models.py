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
    game_title = models.CharField(max_length=50)

    def __str__(self):
        return self.game_title

    class Meta:
        verbose_name_plural = 'Titles'
        ordering = ['game_title']


class Game(models.Model):
    Math_Facts = "Math Facts"
    Anagram_Hunt = "Anagram Hunt"

    GAME_CHOICES = [
        (Math_Facts, "Math Facts"),
        (Anagram_Hunt, "Anagram Hunt"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name='games',
        default=1
    )

    game_title = models.ForeignKey(
        Title, on_delete=models.CASCADE,
        related_name='games'
    )

    title = models.TextField(choices=GAME_CHOICES, default=Math_Facts)
    score = models.SmallIntegerField()
    operation = models.CharField(max_length=3, blank=True)
    max_number = models.SmallIntegerField(blank=True)
    word_length = models.SmallIntegerField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
        # return f'''{self.title, self.score, self.operation,
                    # self.max_number, self.word_length, self.timestamp}'''

    class Meta:
        verbose_name_plural = 'Leaderboard'
