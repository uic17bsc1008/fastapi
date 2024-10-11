from fastapi import FastAPI
from routers import users
import uvicorn
from sqlmodel import SQLModel
from engine import engine
from fastapi.middleware.cors import CORSMiddleware


# Database Config
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Database Config End

# App Config
app = FastAPI()
app.include_router(users.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# App Config End

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

if __name__ == "__main__":
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)