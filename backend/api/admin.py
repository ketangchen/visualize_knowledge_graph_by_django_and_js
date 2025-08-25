# backend/api/admin.py
from django.contrib import admin
from .models import Entity, Relationship  # ���޸���ģ���������Ӧ����

@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # �б�ҳ��ʾ���ֶ�

@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    list_display = ('source', 'name', 'target', 'created_at')