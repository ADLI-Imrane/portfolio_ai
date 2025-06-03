from django.contrib import admin
from django.urls import path, include
from core.views import home
from users.views import CustomPasswordResetView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Surcharge uniquement la vue de reset
    path(
        'accounts/password/reset/',
        CustomPasswordResetView.as_view(),
        name='account_reset_password'
    ),

    # Allauth (email + Google OAuth reste fonctionnel)
    path('accounts/', include('allauth.urls')),

    path('users/', include('users.urls')),
    path('portfolios/', include('portfolios.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('core/', include('core.urls')),
    path('', home, name='home'),
]
