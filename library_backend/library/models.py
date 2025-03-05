from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    isbn = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.JSONField()  # List of genres
    copies = models.IntegerField()
    available_copies = models.IntegerField()
    location = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)
    borrowed_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"
