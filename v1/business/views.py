from rest_framework.generics import ListCreateAPIView

from .models import Business
from .serializers import BusinessSerilizer
from .permisions import HasBusinessAPIKey

class BusinessListCreateAPIView(ListCreateAPIView):
    permission_classes = (HasBusinessAPIKey,)
    serializer_class = BusinessSerilizer
    queryset = Business.objects.all() # pylint: disable=no-member
