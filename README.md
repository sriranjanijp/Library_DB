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
## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sriranjanijp/Library_DB
   cd Library_DB

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Run migrations**:
   ```bash
   python manage.py migrate

4. **Existing User & Token**:
    You can use the following credentials:
    - Username: `testuser`
    - Password: `password123`
    - Token: `46b19f50214164dbe949e5575551c50b1b4a68e9`

5. **Use the token for API requests**:
    Copy the token and use it in your PowerShell API requests like this:
   ```powershell
   (curl -Method Get -Uri "http://127.0.0.1:8000/api/books/" -Headers @{
    "Authorization" = "Token bf336eb6cb8fd567628542299593ff4d5fabc588"
    }).Content | ConvertFrom-Json

## Run the Server

1. **Start the server**:
   ```bash
   python manage.py runserver

2. **Access the API**: 
    `http://127.0.0.1:8000/`

## Some commands

1. **Show all books**
```powershell
   (curl -Method Get -Uri "http://127.0.0.1:8000/api/books/" -Headers @{
    "Authorization" = "Token bf336eb6cb8fd567628542299593ff4d5fabc588"
    }).Content | ConvertFrom-Json
```
2. **To add a book**
```powershell
   $body = @{
    "isbn" = "0-375-70402-7"
    "title" = "Norwegian Wood"
    "author" = "Haruki Murakami"
    "genre" = @("Fiction", "Romance")
    "copies" = 4
    "available_copies" = 4
    "location" = "Section B-14"
    "rating" = 4.2
    "borrowed_count" = 0
} | ConvertTo-Json -Depth 2

curl -Method Post -Uri "http://127.0.0.1:8000/api/books/" -Headers @{
    "Authorization" = "Token bf336eb6cb8fd567628542299593ff4d5fabc588"
    "Content-Type"  = "application/json"
} -Body $body
```


_Last updated: March 5, 2025 [9:00pm]_
