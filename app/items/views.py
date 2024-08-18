from rest_framework import permissions, viewsets

from items.models import Item
from items.serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [
        permissions.AllowAny,
    ]
