from django.urls import path
from . import views

urlpatterns = [
    path('kg/data', views.get_graph_data, name='get_graph_data'),  # ��ȡͼ������
    path('kg/entity', views.add_entity, name='add_entity'),        # ����ʵ��
    # �ɲ��䣺ɾ��ʵ�塢�޸Ĺ�ϵ�Ƚӿ�
]