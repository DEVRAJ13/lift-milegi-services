from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate
from utils.security import hash_password


def create_user(db: Session, data: UserCreate) -> User:
    # 1️⃣ Check if email already exists
    if data.email:
        existing_user = db.query(User).filter(User.email == data.email).first()
        if existing_user:
            raise ValueError("Email already registered")

    # 2️⃣ Create user safely
    user = User(
        email=data.email,
        phone=data.phone,
        password=hash_password(data.password)
    )

    # 3️⃣ Persist to DB
    db.add(user)
    db.commit()
    db.refresh(user)

    return user
