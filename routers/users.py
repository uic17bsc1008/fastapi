from fastapi import APIRouter, status, HTTPException
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

@router.get('/user/details/{user_id}/')
async def get_user(user_id : int, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.get('/user/delete/{user_id}/')
def delete_hero(user_id: int, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"ok": True}