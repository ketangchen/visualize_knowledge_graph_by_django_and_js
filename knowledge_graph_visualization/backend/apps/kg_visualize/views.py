from django.http import JsonResponse
from .models import Entity, Relationship
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt  # ����������ʱ�ر�CSRF��֤
def get_graph_data(request):
    """��ȡ֪ʶͼ���������ݣ�ʵ��+��ϵ��"""
    if request.method == 'GET':
        # ��ѯ����ʵ��
        entities = Entity.objects.all().values("id", "name", "type", "description")
        # ��ѯ���й�ϵ
        relations = Relationship.objects.all().values(
            "id", "source_id", "target_id", "type", "description"
        )
        # ת��ΪD3.js��ʶ��ĸ�ʽ
        graph_data = {
            "nodes": list(entities),
            "links": [
                {
                    "source": r["source_id"],
                    "target": r["target_id"],
                    "type": r["type"],
                    "description": r.get("description", ""),
                    "id": r["id"]
                } for r in relations
            ]
        }
        return JsonResponse({"ret": 0, "data": graph_data})
    return JsonResponse({"ret": 1, "msg": "��֧�ֵ����󷽷�"})


@csrf_exempt
def add_entity(request):
    """����ʵ��"""
    if request.method == 'POST':
        data = json.loads(request.body)
        required_fields = ["id", "name"]
        if not all(field in data for field in required_fields):
            return JsonResponse({"ret": 1, "msg": "ȱ�ٱ�Ҫ�ֶΣ�id��name��"})

        try:
            Entity.objects.create(
                id=data["id"],
                name=data["name"],
                type=data.get("type", ""),
                description=data.get("description", "")
            )
            return JsonResponse({"ret": 0, "msg": "ʵ�崴���ɹ�"})
        except Exception as e:
            return JsonResponse({"ret": 1, "msg": f"����ʧ�ܣ�{str(e)}"})
    return JsonResponse({"ret": 1, "msg": "��֧�ֵ����󷽷�"})