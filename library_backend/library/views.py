from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Book
from .serializers import BookSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

@csrf_exempt
def borrow_book(request):
    if request.method == "POST":
        data = json.loads(request.body)
        book_id = data.get("book_id")

        try:
            book = Book.objects.get(id=book_id)
            if book.available_copies > 0:
                book.available_copies -= 1
                book.borrowed_count += 1
                book.save()
                return JsonResponse({"message": f"You borrowed '{book.title}'. Copies left: {book.available_copies}"})
            else:
                return JsonResponse({"error": "No available copies"}, status=400)
        except Book.DoesNotExist:
            return JsonResponse({"error": "Book not found"}, status=404)

    return JsonResponse({"error": "Invalid request"}, status=400)
