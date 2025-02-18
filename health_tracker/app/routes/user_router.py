from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, field_validator
from app.db.database import SessionLocal
from app.db.models import GenderEnum, SmokingEnum
from app.services.users_service import get_all_users, get_user_by_id, create_user, update_user, delete_user

router = APIRouter()

# Database session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models with validation
class UserCreate(BaseModel):
    name: str
    email: str
    gender: int
    age: int
    smoking_habits: int | None
    weight: float
    height: float

    @field_validator("gender")
    @classmethod
    def validate_gender(cls, value):
        if value not in [g.value for g in GenderEnum]:
            raise ValueError("Gender must be 1 (Male) or 2 (Female)")
        return value

    @field_validator("smoking_habits")
    @classmethod
    def validate_smoking(cls, value):
        if value is not None and value not in [s.value for s in SmokingEnum]:
            raise ValueError("Smoking habits must be 0 (Non-Smoker), 1 (Occasional), or 2 (Heavy Smoker)")
        return value

class UserUpdate(UserCreate):
    pass  # No structural change

# API Endpoints
@router.post("/users")
def create_user_api(user: UserCreate, db: Session = Depends(get_db)):
    """Creates a new user."""
    return create_user(user, db)

@router.get("/users")
def get_users_api(db: Session = Depends(get_db)):
    """Retrieves all users."""
    return get_all_users(db)

@router.get("/users/{user_id}")
def get_user_api(user_id: int, db: Session = Depends(get_db)):
    """Retrieves a user by ID."""
    return get_user_by_id(user_id, db)

@router.put("/users/{user_id}")
def update_user_api(user_id: int, updated_user: UserUpdate, db: Session = Depends(get_db)):
    """Updates user details by ID."""
    return update_user(user_id, updated_user, db)

@router.delete("/users/{user_id}")
def delete_user_api(user_id: int, db: Session = Depends(get_db)):
    """Deletes a user by ID."""
    return delete_user(user_id, db)