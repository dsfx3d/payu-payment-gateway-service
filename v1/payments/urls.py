from django.urls import path

from .views import PreCheckoutView, TransactionCallbackView, TransactionCreateAPIView

urlpatterns = [
    path('checkout/<str:access_key>/<str:txnid>/', PreCheckoutView.as_view(), name='payments_pre_checkout'),
    path('cb/<str:txnid>/', TransactionCallbackView.as_view(), name="payments_callback"),
    path('api/transaction/', TransactionCreateAPIView.as_view(), name="payments_api_txn_create")
]
