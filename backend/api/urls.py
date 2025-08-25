# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

# ����·������ע����ͼ��
router = DefaultRouter()
router.register(r'items', ItemViewSet)

# API URL����
urlpatterns = [
    path('', include(router.urls)),
]
