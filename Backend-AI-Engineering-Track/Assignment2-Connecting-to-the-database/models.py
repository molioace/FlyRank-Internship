from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
from typing import Optional
from pathlib import Path

# Database table
class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    done: bool = False
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    updated_at: Optional[datetime] = None


# Data coming from client
class TaskCreate(SQLModel):
    title: str


# Data for PATCH requests
class TaskUpdate(SQLModel):
    title: Optional[str] = None
    done: Optional[bool] = None

