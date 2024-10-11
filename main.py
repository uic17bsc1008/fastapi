from fastapi import FastAPI
from routers import users
import uvicorn
from sqlmodel import SQLModel
from engine import engine


# Database Config
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# App Config

app = FastAPI()
app.include_router(users.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

if __name__ == "__main__":
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)