import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-^o_0tn=l20bcu(us@)1=w$0xzs_j=uo09q*-pu&q+zk^!d_)f8"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
AUTH_USER_MODEL = 'accounts.User'
# AUTH_USER_MODEL = 'yasha.User'

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',  # Your accounts app
    'djongo', 
    'yasha',
    # Add djongo to installed apps
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

ROOT_URLCONF = 'trevon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'trevon.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'user',
        'CLIENT': {
            'host': 'mongodb+srv://admin:root@yasha.iutjjwd.mongodb.net/?retryWrites=true&w=majority&appName=Yasha',
            # 'tls': True,
            'port': 27017,
            'username': "admin",
            'password': "root",
            # 'authSource': 'admin',
            # 'authMechanism': 'SCRAM-SHA-1',
            # 'tlsAllowInvalidCertificates': True  # If you are using self-signed certificates or need to bypass validation
        }
    }
}   



# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# settings.py

COMPILER_API_URL = 'https://api.jdoodle.com/v1/execute'
COMPILER_API_KEY = '1a1caf708cc5cc29c28c156d88e482b0'

PROBLEM_API_URL = 'https://28fa7403.problems.sphere-engine.com/api/v4'
PROBLEM_API_KEY = '4d22d7088552e3ff458f3706e345c533'

CONTAINER_API_URL = 'https://28fa7403.containers.sphere-engine.com/api/v1'
CONTAINER_API_KEY = '8fbf6b64e8674edcafbf8484c629ac45'

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
