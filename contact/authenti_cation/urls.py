from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView,TokenVerifyView, TokenObtainPairView

from .views import *

urlpatterns=[
    path('register/', RegisterView.as_view()),
    path('login/',TokenObtainPairView.as_view()),
]