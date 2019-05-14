import re

from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

@deconstructible
class CustomUnicodeValidator(validators.RegexValidator):
    regex = r'^[a-zA-Z0-9]{4,}$'
    message = _(
        'Enter a valid username. This value may contain only letters, '
        'numbers.'
    )
    flags = 0
