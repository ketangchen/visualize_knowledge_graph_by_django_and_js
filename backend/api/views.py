# backend/api/views.py
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()  # ��ѯ��������
    serializer_class = ItemSerializer  # �������л���