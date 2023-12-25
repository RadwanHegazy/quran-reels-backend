from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from .apis.register import RegisterView
from .apis.profile import UserProfile


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('register/',RegisterView),
    path('profile/',UserProfile),
]