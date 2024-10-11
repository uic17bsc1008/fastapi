from fastapi import APIRouter, status
from models.users import User
from engine import SessionDep
from sqlmodel import select

router = APIRouter()


@router.post('/create/user/', status_code=status.HTTP_201_CREATED)
async def create_user(user: User, session: SessionDep):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.get('/users/')
async def all_users(session: SessionDep):
    return session.exec(select(User)).all()
