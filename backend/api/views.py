# backend/api/views.py
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()  # 查询所有数据
    serializer_class = ItemSerializer  # 关联序列化器