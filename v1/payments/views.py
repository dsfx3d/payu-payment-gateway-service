import os
from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.generics import CreateAPIView
from payme.hasher import Hasher

from v1.payments.models import Transaction, TransactionAccessKey
from .serilizers import TransactionSerilizer



class TransactionCreateAPIView(CreateAPIView):
    serializer_class = TransactionSerilizer



class PreCheckoutView(View):

    def get(self, request, access_key, txnid):
        access = TransactionAccessKey.objects.filter(id=access_key).first() # pylint: disable=no-member
        if not access:
            return HttpResponse(status=400)

        txn = Transaction.objects.filter(id=txnid).first() # pylint: disable=no-member
        if txn == None:
            return HttpResponse(status=404)

        if txn.id != access.transaction.id:
            return HttpResponse(status=400)

        cburl = request.build_absolute_uri(
            reverse('payments_callback', kwargs=dict(txnid=txn.id))
        )
        context = dict(
            payu_key = txn.business.payu_key,
            txn_hash = txn.txn_hash,
            url = os.getenv('PAYU_URL', 'https://sandboxsecure.payu.in/_payment'),
            txnid = txn.id,
            amount = txn.amount,
            firstname = txn.firstname,
            email = txn.email,
            phone = txn.phone or '',
            productinfo = txn.productinfo,
            surl = cburl,
            furl = f'{cburl}?f=1'
        )
        return render(request, 'pre_checkout.html', context=context)


@method_decorator(csrf_exempt, name='dispatch')
class TransactionCallbackView(View):

    def post(self, request, txnid):
        txnStatus = request.POST.get('status')

        if request  .GET.get('f'):
            return HttpResponse(f'failed: {txnStatus}')

        txn = Transaction.objects.filter(id=txnid).first() # pylint: disable=no-member
        if txn == None:
            return HttpResponse(status=404)

        hasher = Hasher(txn.business.payu_key, txn.business.payu_salt)
        txnSuccess = hasher.check_hash(request.POST)

        if txnSuccess:
            pass
