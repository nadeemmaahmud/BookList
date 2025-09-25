from rest_framework import viewsets
from .serializers import BookSeializer
from .models import Books

class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSeializer