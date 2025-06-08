import os
from pathlib import Path
from dotenv import load_dotenv
import sib_api_v3_sdk

# 📁 Chargement des variables d'environnement
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Clé secrète & debug
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "fallback-secret-key")
DEBUG = os.getenv("DEBUG", "True") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

# 📦 Applications
INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'widget_tweaks',

    # Auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # Custom apps
    'users',
    'portfolios',
    'chatbot',
    'core',
]

SITE_ID = 1

# 🔁 Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'portfolio_ai.urls'

# 📁 Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # requis par allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio_ai.wsgi.application'

# 📊 Base de données
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔐 Validation mot de passe
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🔐 Authentification
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# 🌍 Langue et temps
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 📁 Fichiers statiques & médias
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'static/uploads/'

# 🛠 Paramètres globaux
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 📧 Email via Brevo (ex Sendinblue)
BREVO_API_KEY = os.getenv("BREVO_API_KEY")
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = BREVO_API_KEY

EMAIL_BACKEND = 'core.email_backends.BrevoEmailBackend'
DEFAULT_FROM_EMAIL = "Portfolio AI <themrx.test9@gmail.com>"
ACCOUNT_DEFAULT_FROM_EMAIL = "Portfolio AI <themrx.test9@gmail.com>"


# ⚙️ Allauth
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_SIGNUP_FIELDS = ['email', 'password1', 'password2']
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/portfolios/'
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_SIGNUP = False

ACCOUNT_EMAIL_SUBJECT_PREFIX = "[Portfolio AI] "

# 🔁 Templates personnalisés (utilisés dans l'adapter)
ACCOUNT_EMAIL_CONFIRMATION_SUBJECT_TEMPLATE = "account/email/email_confirmation_subject.txt"
ACCOUNT_EMAIL_CONFIRMATION_HTML_TEMPLATE = "account/email/email_confirmation_message.html"

# ✅ Adapter personnalisé
ACCOUNT_FORMS = { 'signup': 'users.forms.CustomSignupForm' }

DEFAULT_DOMAIN = "localhost:8000"
DEFAULT_PROTOCOL = 'http'