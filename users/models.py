from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


def validate_avatar(value):
    w, h = get_image_dimensions(value)
    if w > 200 or h > 200:
        raise ValidationError('Avatar must be no bigger than 200x200 pixels.')


class CustomUser(AbstractUser):
    dob = models.DateField(
        verbose_name="Date of Birth", null=True, blank=True
    )

    def get_absolute_url(self):
        return reverse('my-account')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.username})'

    avatar = models.ImageField(upload_to='avatars/', blank=True,
        help_text='Image must be 200px by 200px.',
        validators=[validate_avatar]
    )
