import os
from pathlib import Path

# ��Ŀ��Ŀ¼
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ��ȫ��Կ��ʵ�ʲ����������
SECRET_KEY = 'django-insecure-example-key-for-dev-only'

# ���������ر�DEBUG
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Ӧ������
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # �Զ���Ӧ��
    'apps.kg_visualize',  # ֪ʶͼ�׺���Ӧ��
    'apps.common',        # ��������Ӧ��
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

# ģ�����ã�����ǰ��ҳ�棩
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'frontend')],  # ǰ��ҳ��Ŀ¼
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# ���ݿ����ã�Ĭ��SQLite�����滻ΪPostgreSQL��
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ������֤
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
]

# ���ʻ�
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_TZ = True

# ��̬�ļ����ã�CSS/JS�ȣ�
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'frontend/static')]

# Ĭ����������
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'