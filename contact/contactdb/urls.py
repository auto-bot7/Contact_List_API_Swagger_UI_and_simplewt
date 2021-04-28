from django.urls import path
from .views import ContactList, ContactRUD
urlpatterns = [
    path('g_c/', ContactList.as_view()),
    path('update/<int:pk>/', ContactRUD.as_view())
]
