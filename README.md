
# 🚀 FastAPI Authentication Project

A simple and clean authentication system using FastAPI, SQLAlchemy, and JWT tokens.


## 📂 Project Structure

    project_name/
    ├── main.py
    ├── models/
    │   ├── db.py
    │   └── user.py
    ├── routers/
    │   └── auth.py
    ├── requirements.txt


## ✨ Features

 - 🔒 User registration
 - 🔑 User login
 - 🔐 Password hashing with Passlib
 - 🛡️ JWT token generation and validation
 - 👤 Token-based user authentication


## 🛠 Technologies Used
 - FastAPI — modern and high-performance web framework
 - SQLAlchemy — ORM for working with databases
 - PostgreSQL — relational database
 - Pydantic — data validation and serialization
 - Passlib — password hashing
 - Python-Jose — JWT token handling


## 🚀 Getting Started

### 1. Install libraries

```bash
  pip install -r requirements.txt
```

### 2. Run the application
```bash
   fastapi dev main.py
```

### 3. Open the documentation
```bash
    http://127.0.0.1:8000/docs
```
