from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import BookSeializer, FeedbackSerializer
from .models import Books, Feedback
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSeializer
    permission_classes = [IsAdminOrReadOnly]

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)