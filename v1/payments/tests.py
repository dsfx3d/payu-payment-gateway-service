from django.test import TestCase
from django.shortcuts import reverse

from rest_framework import status

from .models import Transaction
from v1.business.models import Business

class PreCheckoutViewTestCase(TestCase):
    # pylint: disable=no-member
    def setUp(self):
        self.business = Business.objects.create(name='Foo Inc.')

        self.txnData = dict(
            amount = 1000,
            productinfo = 'Foo Item',
            firstname = 'Mr. Foo',
            email = 'foo@bazmail.com',
        )
        self.transaction = Transaction.objects.create(
            business = self.business,
            amount = self.txnData['amount'],
            productinfo = self.txnData['productinfo'],
            firstname = self.txnData['firstname'],
            email = self.txnData['email'],
        )

    def test_raises_not_found_if_transaction_not_found(self):
        response = self.client.get(
            reverse(
                'payments_pre_checkout',
                kwargs=dict(access_key=1, txnid=1)
            )
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
