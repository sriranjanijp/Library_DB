from django.urls import path
from .views import BookListCreateView, BookDetailView
from library.views import borrow_book
from .views import return_book

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path("borrow/", borrow_book, name="borrow-book"),
    path("return/", return_book, name="return-book"),
]
