import requests
import json
import pytest

BASE_URL = 'http://localhost:8000/api'

def test_get_graph_data():
    """���Ի�ȡͼ�����ݽӿ�"""
    response = requests.get(f'{BASE_URL}/kg/data')
    assert response.status_code == 200, "�ӿ�����ʧ��"
    data = response.json()
    assert data['ret'] == 0, "�ӿڷ��ش���"
    assert 'nodes' in data['data'] and 'links' in data['data'], "���ݸ�ʽ����"

def test_add_entity():
    """��������ʵ��ӿ�"""
    test_entity = {
        "id": "test_entity_123",
        "name": "����ʵ��",
        "type": "��������"
    }
    print(111)

    response = requests.post(
        f'{BASE_URL}/kg/entity',
        headers={'Content-Type': 'application/json'},
        data=json.dumps(test_entity)
    )
    assert response.status_code == 200, "�ӿ�����ʧ��"
    result = response.json()
    assert result['ret'] == 0, f"����ʵ��ʧ��: {result.get('msg')}"

if __name__ == '__main__':
    pytest.main(['-v', 'test_kg_api.py'])