from pydantic import BaseModel, EmailStr, validator
from datetime import datetime
from typing import Optional
import re


class Contact(BaseModel):
    id: Optional[str] = None
    first_name: str
    last_name: str
    patronymic: str
    phone: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime


class ContactIn(BaseModel):
    # id: Optional[str] = None
    first_name: str
    last_name: str
    patronymic: str
    phone: str
    email: EmailStr

    @validator('phone')
    def phone_validator(cls, v, values, **kwargs):
        regex = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"
        if v and not re.search(regex, v, re.I):
            raise ValueError("Phone Number Invalid.")
        return v
