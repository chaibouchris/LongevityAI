from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services.blood_test_service import (
    create_blood_test, get_all_blood_tests, get_blood_test_by_id, delete_blood_test,
    BloodTestCreate, BloodTestResponse
)

router = APIRouter()

# Database session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a blood test record
@router.post("/blood_tests", response_model=BloodTestResponse)
def create_blood_test_route(test: BloodTestCreate, db: Session = Depends(get_db)):
    """Creates a new blood test record."""
    return create_blood_test(db, test)

# Retrieve all blood test records
@router.get("/blood_tests", response_model=list[BloodTestResponse])
def get_blood_tests_route(db: Session = Depends(get_db)):
    """Retrieves all blood test records."""
    return get_all_blood_tests(db)

# Retrieve a specific blood test record by ID
@router.get("/blood_tests/{test_id}", response_model=BloodTestResponse)
def get_blood_test_route(test_id: int, db: Session = Depends(get_db)):
    """Retrieves a blood test record by its ID."""
    return get_blood_test_by_id(db, test_id)

# Delete a blood test record
@router.delete("/blood_tests/{test_id}", response_model=dict)
def delete_blood_test_route(test_id: int, db: Session = Depends(get_db)):
    """Deletes a blood test record by its ID."""
    return delete_blood_test(db, test_id)