from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.db import getDb as get_db

from schemas.auth import LoginRequest, TokenResponse
from controllers.auth_controller import login_controller

router = APIRouter(tags=["Auth"])

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    try:
        token = login_controller(db, data.email, data.password)
        return {"access_token": token}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )
