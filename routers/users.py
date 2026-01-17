from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.db import getDb as get_db
from schemas.user import UserCreate, UserResponse
from controllers.users_controller import create_user_controller

router = APIRouter(tags=["Auth"])

@router.post(
    "/signup",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_user_controller(db, user)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

