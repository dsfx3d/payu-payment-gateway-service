from uuid import uuid4
from django.db import models
from django.utils.translation import ugettext_lazy as _

from payme.hasher import Hasher
from django_mysql.models import EnumField

from v1.business.models import Business



def keygen_hex(length=30):
    txnid = uuid4()
    return txnid.hex[:length]


class Transaction(models.Model):
    STAUS_ENUM = ('request', 'success', 'failure')
    CURRENCY_ENUM = (
        ('INR', 'Indian Rupees'),
    )

    id = models.CharField(max_length=30, primary_key=True, default=keygen_hex)
    status = EnumField(choices=STAUS_ENUM, default=STAUS_ENUM[0])
    currency = EnumField(_('Currency'), choices=CURRENCY_ENUM, default=CURRENCY_ENUM[0][0])
    business = models.ForeignKey(Business, verbose_name=_('Business'), on_delete=models.DO_NOTHING)
    amount = models.FloatField(_('Amount'))
    productinfo = models.TextField(_('Product Info'))
    firstname = models.CharField(_('First Name'), max_length=50)
    lastname = models.CharField(_('Last Name'), max_length=50, null=True, blank=True)
    email = models.EmailField(_('Email'), max_length=254)
    phone = models.CharField(_('Phone'), max_length=50, null=True, blank=True)
    address1 = models.CharField(_('Address 1'), max_length=100, null=True, blank=True)
    address2 = models.CharField(_('Address 2'), max_length=100, null=True, blank=True)
    city = models.CharField(_('City'), max_length=50, null=True, blank=True)
    state = models.CharField(_('State'), max_length=50, null=True, blank=True)
    country = models.CharField(_('Country'), max_length=50, null=True, blank=True)
    zipcode = models.CharField(_('Zip Code'), max_length=50, null=True, blank=True)
    udf1 = models.TextField(_('user defined 1'), blank=True, null=True)
    udf2 = models.TextField(_('user defined 2'), blank=True, null=True)
    udf3 = models.TextField(_('user defined 3'), blank=True, null=True)
    udf4 = models.TextField(_('user defined 4'), blank=True, null=True)
    udf5 = models.TextField(_('user defined 5'), blank=True, null=True)

    @property
    def txn_hash(self):
        if self.business is None:
            return None
        hasher = Hasher(self.business.payu_key, self.business.payu_salt) # pylint: disable=no-member
        payload = dict(
            txnid = self.id,
            amount = self.amount,
            productinfo = self.productinfo,
            firstname = self.firstname,
            email = self.email,
            udf1 = self.udf1,
            udf2 = self.udf2,
            udf3 = self.udf3,
            udf4 = self.udf4,
            udf5 = self.udf5
        )
        return hasher.generate_hash(payload)


class TransactionAccessKey(models.Model):
    id = models.UUIDField(_("key"), primary_key=True, default=uuid4)
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE, related_name='access_key')
