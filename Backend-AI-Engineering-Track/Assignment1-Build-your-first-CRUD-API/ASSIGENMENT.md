# W2 · A1 — Build Your First CRUD API 🚀

A FastAPI-based Task Management API built as part of the **FlyRank Internship** (Backend AI Engineering Track).

This project demonstrates the fundamentals of backend development by implementing a complete **CRUD API** (Create, Read, Update, Delete) using **FastAPI**, with in-memory data storage and interactive API documentation through **Swagger UI**.

---

## 📌 Assignment Overview

The goal of this assignment was to build a small API that manages a to-do list.

The API supports the four core backend operations:

| Operation | HTTP Method | Endpoint | Description |
|---|---|---|---|
| Create | POST | `/tasks` | Add a new task |
| Read | GET | `/tasks` | Get all tasks |
| Read | GET | `/tasks/{id}` | Get a specific task |
| Update | PUT | `/tasks/{id}` | Update a task |
| Delete | DELETE | `/tasks/{id}` | Remove a task |

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **Pydantic**
- **Swagger UI / OpenAPI**
- **Git & GitHub**

---

## ✨ Features

✅ Complete CRUD functionality  
✅ REST API architecture  
✅ In-memory task storage  
✅ Request validation using Pydantic models  
✅ Proper HTTP status codes  
✅ Error handling for invalid requests  
✅ Interactive API documentation using Swagger UI  

---

## 📂 Project Structure

```
.
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Running

### 1. Clone the repository

```bash
git clone <repository-url>
cd <project-folder>
```

### 2. Create and activate virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API server

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://localhost:8000
```

---

# 📖 API Documentation

FastAPI automatically generates Swagger UI documentation.

Open:

```
http://localhost:8000/docs
```

From Swagger UI you can test:

- Creating tasks
- Reading tasks
- Updating tasks
- Deleting tasks

---

# 🔌 API Endpoints

## Root Endpoint

### GET `/`

Returns information about the API.

Example response:

```json
{
  "name": "Task API",
  "version": "1.0",
  "endpoints": [
    "/tasks"
  ]
}
```

---

## Health Check

### GET `/health`

Checks if the server is running.

Response:

```json
{
  "status": "ok"
}
```

---

# Tasks API

## Get All Tasks

### GET `/tasks`

Response:

```json
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "done": false
  }
]
```

---

## Get Single Task

### GET `/tasks/{id}`

Example:

```
GET /tasks/1
```

Success:

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "done": false
}
```

If task does not exist:

Status:

```
404 Not Found
```

Response:

```json
{
  "error": "Task not found"
}
```

---

## Create Task

### POST `/tasks`

Request body:

```json
{
  "title": "Build CRUD API"
}
```

Response:

```json
{
  "id": 4,
  "title": "Build CRUD API",
  "done": false
}
```

Status:

```
201 Created
```

Invalid request:

```
400 Bad Request
```

---

## Update Task

### PUT `/tasks/{id}`

Example:

```
PUT /tasks/1
```

Request:

```json
{
  "title": "Complete FastAPI assignment",
  "done": true
}
```

Response:

```json
{
  "id": 1,
  "title": "Complete FastAPI assignment",
  "done": true
}
```

---

## Delete Task

### DELETE `/tasks/{id}`

Example:

```
DELETE /tasks/1
```

Success response:

```
204 No Content
```

Unknown task:

```
404 Not Found
```

---

# 🧪 Testing

Example using curl:

### Create Task

```bash
curl -i -X POST http://localhost:8000/tasks \
-H "Content-Type: application/json" \
-d '{"title":"Buy milk"}'
```

Example response:

```
HTTP/1.1 201 Created
```

---

# 💾 Data Storage

This project uses **in-memory storage**.

Tasks are stored inside a Python list while the server is running.

Example:

```python
tasks = []
```

Because there is no database:

- Data is lost after restarting the server.
- This is intentional for learning CRUD fundamentals.

---

# 🤖 AI Rematch (Optional)

For the bonus stage, an AI assistant was asked to generate the same API.

The generated solution was reviewed and compared against the manually built version.

Comparison included:

- Differences in implementation
- Missing requirements
- Improvements to the AI prompt

---

# 🎯 Learning Outcomes

Through this assignment I practiced:

- Building REST APIs with FastAPI
- Understanding HTTP methods
- Working with request/response cycles
- Validating API inputs
- Handling HTTP status codes
- Creating API documentation
- Using Git and GitHub for project publishing

---

## 📌 Assignment Source

FlyRank Internship  
Backend AI Engineering Track  
Week 2 — Assignment 1: Build Your First CRUD API