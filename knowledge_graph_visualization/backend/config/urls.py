from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),  # Django�����̨
    path('', TemplateView.as_view(template_name='index.html')),  # ǰ�����ҳ��
    path('api/', include('apps.kg_visualize.urls')),  # ֪ʶͼ��API·��
]