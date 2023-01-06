from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    # path('register/', views.RegisterFormView.as_view),
    # path('login', views.LoginFormView.as_view),
    # path('logout', views.LogoutView.as_view),
    # path('forgotpassword', views.ForgotPasswordForm.as_view),
    # path('password_change', views.PasswordChangeForm.as_view),
]
