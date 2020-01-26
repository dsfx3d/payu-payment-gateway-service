from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('v1.business.urls')),
    path('payments/v1/', include('v1.payments.urls')),
]
