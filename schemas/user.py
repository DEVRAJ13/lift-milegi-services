from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    phone: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    uuid: str
    email: Optional[EmailStr]
    phone: Optional[str]
    status: str
    created_at: datetime

    class Config:
        form_attributes = True
