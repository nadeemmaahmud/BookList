from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title