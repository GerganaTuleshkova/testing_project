from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from testing_project.helpers.validators import has_letters_only_validator


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[has_letters_only_validator],
    )

    last_name = models.CharField(
        max_length=25,
        validators=[has_letters_only_validator],
    )

    age = models.IntegerField(
        validators=(
            MinValueValidator(0),
            MaxValueValidator(150),
        )
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
