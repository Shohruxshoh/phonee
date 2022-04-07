from django.urls import path, re_path
from knox import views as knox_views
from .views import ValidatePhoneSendOTP, ValidateOTP, Register, LoginAPI

urlpatterns = [
    path('validate_phone/', ValidatePhoneSendOTP.as_view()),
    path('validate_otp/', ValidateOTP.as_view()),
    path('register/', Register.as_view()),
    path('login/', LoginAPI.as_view()),
    path('logout/', knox_views.LogoutView.as_view()),
]
