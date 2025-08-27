from django.db import models

class Entity(models.Model):
    """֪ʶͼ��ʵ�壨���������ص�ȣ�"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name="ʵ��ID")
    name = models.CharField(max_length=100, verbose_name="ʵ������")
    type = models.CharField(max_length=50, verbose_name="ʵ������", blank=True)  # ��"����"��"��֯"
    description = models.TextField(verbose_name="ʵ������", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="����ʱ��")

    class Meta:
        verbose_name = "֪ʶʵ��"
        verbose_name_plural = "֪ʶʵ��"

    def __str__(self):
        return f"{self.name} ({self.type})"

class Relationship(models.Model):
    """ʵ���Ĺ�ϵ"""
    source = models.ForeignKey(
        Entity,
        on_delete=models.CASCADE,
        related_name="out_relations",
        verbose_name="Դʵ��"
    )
    target = models.ForeignKey(
        Entity,
        on_delete=models.CASCADE,
        related_name="in_relations",
        verbose_name="Ŀ��ʵ��"
    )
    type = models.CharField(max_length=100, verbose_name="��ϵ����")  # ��"����"��"����"
    description = models.TextField(verbose_name="��ϵ����", blank=True)

    class Meta:
        verbose_name = "ʵ���ϵ"
        verbose_name_plural = "ʵ���ϵ"

    def __str__(self):
        return f"{self.source.name} -[{self.type}]-> {self.target.name}"