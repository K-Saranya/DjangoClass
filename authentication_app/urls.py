from django.urls import path
from .views import *


urlpatterns = [
    path('token/', UserSignupAPI.as_view()),
    path('user/token/obtain/', UserLoginAPI.as_view()),
    path("external", external_api_data)
]
