# Library Project README

## Project Overview
A Django REST API for managing a library system, allowing users to view, borrow, and track books.
This project was done with the help of chatGPT because I have no prior knowledge of DB management or using APIs  

## Progress So Far

### 1. **Project Setup**
- Created a Django project and app (`library_backend`).
- Configured `INSTALLED_APPS` to include `rest_framework`.
- Set up a virtual environment and installed dependencies.

### 2. **Model Implementation**
- Defined `Book` model with attributes:
  - `isbn`, `title`, `author`, `genre`, `copies`, `available_copies`, `location`, `rating`, `borrowed_count`.
- Applied migrations to create database.

### 3. **API Development**
- Implemented endpoints:
  - `GET /api/books/` - Retrieve all books.
  - `GET /api/books/<id>/` - Retrieve book details.
  - `POST /api/borrow/` - Borrow a book.
- Used Django REST Framework’s `ListCreateAPIView` and `RetrieveUpdateDestroyAPIView` for book management.
- Added authentication using Tokens

### 4. **Authentication & Security**
- Created a superuser.
- Added CSRF exemption for borrowing books.

### 5. **Testing & Debugging**
- Used Thunder Client and PowerShell `Invoke-WebRequest` for API testing.
- Successfully retrieved book details and verified borrowing logic.
- Debugged authentication issues.

## Next Steps
- Implement user authentication and registration.
- Improve error handling and API responses.

---
_Last updated: March 5, 2025 [9:00pm]_