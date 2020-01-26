from django.db import models
from django.utils.translation import ugettext_lazy as _

from rest_framework_api_key.models import AbstractAPIKey, BaseAPIKeyManager
from rest_framework_api_key.crypto import KeyGenerator

from payment_gateway.lib.models import TimestampMixin


class Business(TimestampMixin, models.Model):
    name = models.CharField(_("Name"), max_length=50)
    active = models.BooleanField(_("active"), default=False)
    payu_key = models.CharField(_("PayU Key"), max_length=50)
    payu_salt = models.CharField(_("PayU Salt"), max_length=50)

    class Meta:
        verbose_name_plural = 'Businesses'

    def __str__(self):
        return f'{self.name}'

class BusinessAPIKeyManager(BaseAPIKeyManager):
    key_generator = KeyGenerator(prefix_length=8, secret_key_length=32)
    def get_usable_keys(self):
        return super().get_usable_keys().filter(business__active=True)

class BusinessAPIKey(AbstractAPIKey):
    objects = BaseAPIKeyManager()
    business = models.ForeignKey(Business, on_delete=models.CASCADE)

class Location(TimestampMixin, models.Model):
    name = models.CharField(_("Name"), max_length=50)
    active = models.BooleanField(_("active"), default=False)
    business = models.ForeignKey(Business, verbose_name=_("Business"), on_delete=models.CASCADE)
