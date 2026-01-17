from sqlalchemy.orm import Session
from services.auth_service import login_user

def login_controller(db: Session, email: str, password: str):
    return login_user(db, email, password)
