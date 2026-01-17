from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Enum,
    TIMESTAMP,
    func
)
from db.db import Base
import uuid

class User(Base):
    __tablename__ = "users"

    id = Column(
        BigInteger,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    uuid = Column(
        String(36),
        unique=True,
        nullable=False,
        default=lambda: str(uuid.uuid4())
    )

    email = Column(
        String(255),
        unique=True,
        nullable=True
    )

    phone = Column(
        String(20),
        unique=True,
        nullable=True
    )

    password = Column(
        String(255),
        nullable=True
    )

    status = Column(
        Enum("ACTIVE", "SUSPENDED", "DELETED", name="user_status"),
        nullable=False,
        default="ACTIVE"
    )

    created_at = Column(
        TIMESTAMP,
        nullable=False,
        server_default=func.current_timestamp()
    )

    deleted_at = Column(
        TIMESTAMP,
        nullable=True
    )