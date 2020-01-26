from rest_framework import serializers

from .models import Transaction, TransactionAccessKey

class TransactionSerilizer(serializers.ModelSerializer):
    access_key = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Transaction
        fields = (
            'id',
            'business',
            'amount',
            'productinfo',
            'firstname',
            'lastname',
            'email',
            'phone',
            'address1',
            'address2',
            'city',
            'state',
            'country',
            'zipcode',
            'udf1',
            'udf2',
            'udf3',
            'udf4',
            'udf5',
            'access_key',
        )

    def create(self, *args, **kwargs):
        txn = super().create(*args, **kwargs)
        TransactionAccessKey.objects.create(transaction=txn) # pylint: disable=no-member
        return txn

