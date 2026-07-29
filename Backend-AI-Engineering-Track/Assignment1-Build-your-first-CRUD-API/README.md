# FastAPI CRUD API Assignment 🚀

A simple CRUD API built using **FastAPI** as part of the FlyRank Internship Backend AI Engineering track.

This project demonstrates the basics of creating API endpoints, handling requests, validating data with Pydantic, and performing CRUD operations using in-memory storage.

## 🛠️ Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn

## 📌 Features

- Create users
- Read all users
- Read a single user by ID
- Update users
- Error handling for missing users
- Data validation using Pydantic models

## 📂 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/users` | Get all users |
| GET | `/users/{id}` | Get user by ID |
| POST | `/users/{id}` | Create a new user |
| PUT | `/users/{id}` | Update an existing user |

## ▶️ Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn main:app --reload
```

Open the API documentation:

```
http://127.0.0.1:8000/docs
```

## 📚 Notes

- The data is stored in memory using a Python dictionary.
- Data will be lost when the server restarts.
- This project was created to practise building REST APIs with FastAPI.