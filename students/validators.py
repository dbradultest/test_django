import datetime
from django.core.exceptions import ValidationError


def adult_validator(birthdate):
    ADULT_AGE_LIMIT = 18

    age = datetime.datetime.now().year - birthdate.year

    if age < ADULT_AGE_LIMIT:
        raise ValidationError(f'Age should be greater than {ADULT_AGE_LIMIT} y.o.')
