from django.core.exceptions import ValidationError


def has_letters_only_validator(value):

    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must contain only letters')

    return value
