from sqlmodel import SQLModel, create_engine, Session

sqlite_file = "tasks.db"

engine = create_engine(
    f"sqlite:///{sqlite_file}",
    connect_args={"check_same_thread": False}
)


def create_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session