# Task API with FastAPI, SQLModel & PostgreSQL

A simple CRUD API built with **FastAPI**, **SQLModel**, and **PostgreSQL**.

The application allows users to create, read, update, and delete tasks while storing data in a PostgreSQL database running inside Docker.

---

## What is this?

This project is a REST API for managing a task list.

It demonstrates:

- Building APIs with FastAPI
- Database modeling using SQLModel
- PostgreSQL database integration
- Docker containerization
- Docker Compose orchestration

The project contains two containers:

- **API container** → FastAPI application
- **Database container** → PostgreSQL database

---

# How to Run Everything

## 1. Clone the repository

```bash
git clone <your-repository-url>
cd Assignment3-Containerize-your-stack
```

---

## 2. Create environment variables

Copy `.env.example`:

```bash
cp .env.example .env
```

Then update the values inside `.env`.

Required variables:

| Variable | Description | Example |
|---|---|---|
| POSTGRES_USER | Database username | postgres |
| POSTGRES_PASSWORD | Database password | dev |
| POSTGRES_DB | Database name | tasks |
| POSTGRES_HOST | Database service name | db |
| POSTGRES_PORT | Database port | 5432 |

---

## 3. Run the application

Start both FastAPI and PostgreSQL with one command:

```bash
docker compose up
```

The API will be available at:

```
http://localhost:3000
```

Swagger documentation:

```
http://localhost:3000/docs
```

---

# API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{id}` | Get a task by ID |
| POST | `/tasks` | Create a new task |
| PATCH | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

---

# Example Request

Create a task:

```bash
curl -i -X POST http://localhost:3000/tasks \
-H "Content-Type: application/json" \
-d '{"title":"Finish Docker assignment","done":false}'
```

Example response:

```json
{
  "id": 1,
  "title": "Finish Docker assignment",
  "done": false,
  "created_at": "2026-08-01T13:14:39",
  "updated_at": null
}
```

---

# Database

The PostgreSQL database runs inside the Docker container.

To access PostgreSQL:

```bash
docker exec -it assignment3-containerize-your-stack-db-1 psql -U postgres -d tasks
```

List tables:

```sql
\dt
```

Example output:

```
        List of relations
 Schema | Name | Type  | Owner
--------+------+-------+----------
 public | task | table | postgres
```

View stored tasks:

```sql
SELECT * FROM task;
```

Example result:

```
 id | title   | done | created_at              | updated_at
----+---------+------+------------------------+------------------------
  2 | stage 2 | f    | 2026-08-01 13:14:47     |
  3 | stage 3 | f    | 2026-08-01 13:14:52     |
  1 | stage 1 | t    | 2026-08-01 13:14:39     | 2026-08-01 13:15:19
```

Database screenshot:

![PostgreSQL Database](database-screenshot.png)

---

# Project Structure

```
.
├── app.py
├── db.py
├── models.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

---

# Features

- Create tasks
- Retrieve all tasks
- Retrieve task by ID
- Update tasks
- Delete tasks
- PostgreSQL persistence
- Dockerized deployment
- Automatic table creation using SQLModel

---

# Stop the Application

```bash
docker compose down
```

Remove containers and database volume:

```bash
docker compose down -v
```