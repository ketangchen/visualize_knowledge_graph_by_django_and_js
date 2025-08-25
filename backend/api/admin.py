# backend/api/admin.py
from django.contrib import admin
from .models import Entity, Relationship  # 若修改了模型名，需对应调整

@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # 列表页显示的字段

@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    list_display = ('source', 'name', 'target', 'created_at')