from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer

User = get_user_model()

class UserCreateViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer