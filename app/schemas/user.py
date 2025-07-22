# app/schemas/user.py

from pydantic import BaseModel, EmailStr, Field, validator
from datetime import datetime, date
from typing import Optional

from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from app.models.User import User
from app.models.modelChoices import userGenderChoices, userNationalityChoices, userCountryOfAsylumChoices

# Generate base schema from model
UserCreateBase = sqlalchemy_to_pydantic(User, exclude=["ID", "CreatedAt", "UpdatedAt"])

class UserCreate(UserCreateBase):
    EmailAddress: EmailStr

    # --- Custom Validators ---
    @validator("DateOfBirth")
    def validate_dob(cls, v):
        if v > datetime.now():
            raise ValueError("Date of birth cannot be in the future.")
        return v

    @validator("PhoneNumber")
    def validate_phone_number(cls, v):
        if not v.isdigit():
            raise ValueError("Phone number must contain only digits.")
        if len(v) < 7 or len(v) > 15:
            raise ValueError("Phone number must be between 7 and 15 digits.")
        return v

    @validator("Gender")
    def validate_gender(cls, v):
        allowed = userGenderChoices
        if v not in allowed:
            raise ValueError(f"Gender must be one of {allowed}")
        return v

    @validator("Nationality")
    def validate_nationality(cls, v):
        allowed = userNationalityChoices
        if v not in allowed:
            raise ValueError(f"Nationality must be one of {allowed}")
        return v
    
    @validator("CountryOfAsylum")
    def validate_country_codes(cls, v):
        allowed = userCountryOfAsylumChoices
        if v not in allowed:
            raise ValueError(f"Country of asylum must be one of {allowed}")
        return v
    

class UserResponse(BaseModel):
    ID: int
    EmailAddress: EmailStr
    Name: str
    Surname: str

    class Config:
        orm_mode = True
