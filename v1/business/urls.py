from django.urls import path

from . import views

urlpatterns = [
    path('business/', views.BusinessListCreateAPIView.as_view(), name='business_list_create')
]
