# app/controllers/signup.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.models.User import User
from app.db.database import get_db
from sqlalchemy.exc import IntegrityError

router = APIRouter()

@router.post("/api/signup", response_model = UserResponse, status_code = status.HTTP_201_CREATED)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(User).filter(User.EmailAddress == user.EmailAddress).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists."
        )

    new_user = User(**user.dict())

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Database constraint error.")

    return new_user
