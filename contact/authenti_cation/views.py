from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.conf import settings
from django.contrib import auth
import jwt

class RegisterView(GenericAPIView):
    serializer_class=UserSerializer
    def post(self,request):
        if request.method=="POST":
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

