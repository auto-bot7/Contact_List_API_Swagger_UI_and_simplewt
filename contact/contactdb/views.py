from django.shortcuts import render
from .models import Contact
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ContactSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class ContactList(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class= ContactSerializer
    def owner_create(self,serializer):
        serializer.save(owner=self.request.user)
     
    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)
    # display owner from User where owner is current user


class ContactRUD(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=ContactSerializer
    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)