from rest_framework_api_key.permissions import BaseHasAPIKey
from .models import BusinessAPIKey

class HasBusinessAPIKey(BaseHasAPIKey):
    model = BusinessAPIKey
