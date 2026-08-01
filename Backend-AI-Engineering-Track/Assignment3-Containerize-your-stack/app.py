from fastapi import FastAPI, HTTPException, Depends, Response
from sqlmodel import Session, select

from models import Task, TaskCreate, TaskUpdate
from db import create_db, get_session
from contextlib import asynccontextmanager
from datetime import datetime, timezone




@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code that runs when the app starts
    create_db()

    yield


app = FastAPI(lifespan=lifespan)



@app.get("/")
def index():
    return {"hello": "world"}


@app.get("/tasks")
def get_tasks(
    session: Session = Depends(get_session)
):
    tasks = session.exec(select(Task)).all()
    return tasks


@app.get("/tasks/{id}")
def get_task(
    id: int,
    session: Session = Depends(get_session)
):
    task = session.get(Task, id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="task not found"
        )

    return task


@app.post("/tasks")
def add_task(
    task: TaskCreate,
    session: Session = Depends(get_session)
):

    db_task = Task(
        title=task.title
    )

    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return db_task

@app.put("/tasks/{id}")
def update_task(
    id: int,
    task: Task,
    session: Session = Depends(get_session)
):

    db_task = session.get(Task, id)

    if not db_task:
        raise HTTPException(404, "task not found")


    db_task.title = task.title
    db_task.done = task.done
    db_task.updated_at = datetime.now(timezone.utc)


    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return db_task


@app.patch("/tasks/{id}")
def patch_task(
    id: int,
    task: TaskUpdate,
    session: Session = Depends(get_session)
):

    db_task = session.get(Task, id)

    if not db_task:
        raise HTTPException(404, "task not found")


    if task.title is not None:
        db_task.title = task.title

    if task.done is not None:
        db_task.done = task.done


    db_task.updated_at = datetime.now(timezone.utc)

    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return db_task



@app.delete("/tasks/{id}", status_code=204)
def delete_task(
    id: int,
    session: Session = Depends(get_session)
):
    task = session.get(Task, id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="task not found"
        )

    session.delete(task)
    session.commit()

    return Response(status_code=204)