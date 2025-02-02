from django.conf import settings
from django.db import models

from nanoid import generate


DEFAULT_ALPHABET = (
    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz-"  # noqa: 501
)
DEFAULT_SIZE = 21


class NanoidField(models.CharField):
    def __init__(self, *args, **kwargs) -> None:
        self.alphabet = kwargs.pop(
            "alphabet", getattr(settings, "NANOID_ALPHABET", DEFAULT_ALPHABET)
        )
        kwargs["max_length"] = kwargs.pop(
            "max_length", getattr(settings, "NANOID_SIZE", DEFAULT_SIZE)
        )
        kwargs["default"] = self.nanoid

        super(NanoidField, self).__init__(*args, **kwargs)

    def nanoid(self):
        return generate(self.alphabet, self.max_length)

    def get_internal_type(self):
        return "CharField"

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['alphabet'] = self.alphabet
        kwargs['max_length'] = self.max_length
        kwargs.pop('default', None)

        return name, path, args, kwargs
