from fastapi import Depends
from typing import Annotated
from sqlmodel import create_engine
from sqlmodel import Session

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///./{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]