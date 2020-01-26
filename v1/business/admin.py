from django.contrib import admin

from rest_framework_api_key.models import APIKey as BaseAPIKey
from rest_framework_api_key.admin import APIKeyModelAdmin


from . import models


admin.site.unregister(BaseAPIKey)

class APIKeyInline(admin.TabularInline):
    model = models.BusinessAPIKey
    min_num = 1
    max_num = 5

class LocationInline(admin.TabularInline):
    model = models.Location

@admin.register(models.Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active')
    inlines = (LocationInline, APIKeyInline)

@admin.register(models.BusinessAPIKey)
class APIKeyAdmin(APIKeyModelAdmin):
    pass


@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active')
