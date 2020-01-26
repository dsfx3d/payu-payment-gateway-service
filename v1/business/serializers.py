from rest_framework import serializers

from . import models

class BusinessSerilizer(serializers.ModelSerializer):
    class Meta:
        model = models.Business
        fields = '__all__'
