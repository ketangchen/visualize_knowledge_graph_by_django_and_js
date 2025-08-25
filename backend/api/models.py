# backend/api/models.py
from django.db import models

class Entity(models.Model):  # �滻ԭItem����ʾ֪ʶͼ�׽ڵ�
    name = models.CharField(max_length=100, verbose_name="entityName")
    description = models.TextField(blank=True, verbose_name="describe")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Relationship(models.Model):  # ��ʾʵ����ϵ
    source = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name="out_relationships", verbose_name="sourceEntity")
    target = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name="in_relationships", verbose_name="targetEntity")
    name = models.CharField(max_length=100, verbose_name="relationName")  # �硰�����������ڡ�
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source.name} {self.name} {self.target.name}"