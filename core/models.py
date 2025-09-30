from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Books(models.Model):
    title = models.CharField(max_length=200)
    plot = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=100)
    release_date = models.DateField(null=True, blank=True)
    book_image = models.ImageField(upload_to='book_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Feedback(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='feedbacks')
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user", "book")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} {self.rating} {self.comment[:50]}"