from django.contrib import admin
from django.urls import path, include
from core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('portfolios/', include('portfolios.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('', home, name='home'),
]
