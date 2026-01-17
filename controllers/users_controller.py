from sqlalchemy.orm import Session
from schemas.user import UserCreate
from services.users_service import create_user

def create_user_controller(db: Session, user: UserCreate):
    return create_user(db, user)
