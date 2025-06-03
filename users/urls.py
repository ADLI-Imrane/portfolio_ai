from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView  # importe ta vue personnalisée

urlpatterns = [
    path(
        'accounts/password/reset/',
        CustomPasswordResetView.as_view(),
        name='password_reset',
    ),
    path(
        'accounts/password/reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='account/password/password_reset_done.html',
        ),
        name='password_reset_done',
    ),
    path(
        'accounts/password/reset/confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='account/password/password_reset_confirm.html',
        ),
        name='password_reset_confirm',
    ),
    path(
        'accounts/password/reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='account/password/password_reset_complete.html',
        ),
        name='password_reset_complete',
    ),
]
