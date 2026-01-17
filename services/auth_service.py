from sqlalchemy.orm import Session
from models.user import User
from utils.security import verify_password
from utils.jwt import create_access_token

def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise ValueError("Invalid credentials")

    if user.status != "ACTIVE":
        raise ValueError("User account is not active")

    if not verify_password(password, user.password):
        raise ValueError("Invalid credentials")

    token = create_access_token({"sub": str(user.id)})

    return token
