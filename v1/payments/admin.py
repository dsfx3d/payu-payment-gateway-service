from django.contrib import admin

from .models import Transaction

def txn_amount(obj):
    return f'{obj.amount} {obj.currency}'
txn_amount.short_description = 'Amount'

def payee(obj):
    return f'{obj.firstname} {obj.lastname}'

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'business', payee, txn_amount)
