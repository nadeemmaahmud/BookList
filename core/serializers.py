from rest_framework import serializers
from .models import Books, Feedback

class BookSeializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    
    class Meta:
        model = Feedback
        fields = ["id", "user", "book", "rating", "comment", "created_at", "updated_at"]