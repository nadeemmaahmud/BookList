from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer
from .permissions import IsAdminOrSelf

User = get_user_model()

class UserCreateViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    def get_permissions(self):
        if self.action == "create":
            return [permissions.AllowAny()]
        elif self.action == "list":
            return [permissions.IsAdminUser()]
        else:
            return [IsAdminOrSelf()]