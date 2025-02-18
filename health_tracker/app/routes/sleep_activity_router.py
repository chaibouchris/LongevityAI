from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services.sleep_activity_service import (
    create_sleep_record, get_all_sleep_records, get_sleep_record_by_id, delete_sleep_record,
    SleepActivityCreate, SleepActivityResponse
)

router = APIRouter()

# Database session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a sleep activity record
@router.post("/sleep_activity", response_model=SleepActivityResponse)
def create_sleep_activity_route(sleep: SleepActivityCreate, db: Session = Depends(get_db)):
    """Creates a new sleep activity record."""
    return create_sleep_record(db, sleep)

# Retrieve all sleep activity records
@router.get("/sleep_activity", response_model=list[SleepActivityResponse])
def get_sleep_activities_route(db: Session = Depends(get_db)):
    """Retrieves all sleep activity records."""
    return get_all_sleep_records(db)

# Retrieve a specific sleep activity record by ID
@router.get("/sleep_activity/{sleep_id}", response_model=SleepActivityResponse)
def get_sleep_activity_route(sleep_id: int, db: Session = Depends(get_db)):
    """Retrieves a sleep activity record by its ID."""
    return get_sleep_record_by_id(db, sleep_id)

# Delete a sleep activity record
@router.delete("/sleep_activity/{sleep_id}", response_model=dict)
def delete_sleep_activity_route(sleep_id: int, db: Session = Depends(get_db)):
    """Deletes a sleep activity record by its ID."""
    return delete_sleep_record(db, sleep_id)
