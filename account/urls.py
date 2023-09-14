from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_view, logout_view, password_reset

from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


app_name = 'account'

urlpatterns = [path('', login_view ,name='login'),
               path('logout/', logout_view , name= 'logout'),
               path('password_reset/', PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
               path('password-reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
               path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
               path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),

                 ]