from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services.physical_activity_service import (
    create_activity, get_all_activities, get_activity_by_id, delete_activity,
    PhysicalActivityCreate, PhysicalActivityResponse
)

router = APIRouter()

# Database session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a physical activity record
@router.post("/physical_activity", response_model=PhysicalActivityResponse)
def create_physical_activity_route(activity: PhysicalActivityCreate, db: Session = Depends(get_db)):
    """Creates a new physical activity record."""
    return create_activity(db, activity)

# Retrieve all physical activity records
@router.get("/physical_activity", response_model=list[PhysicalActivityResponse])
def get_physical_activities_route(db: Session = Depends(get_db)):
    """Retrieves all physical activity records."""
    return get_all_activities(db)

# Retrieve a specific physical activity record by ID
@router.get("/physical_activity/{activity_id}", response_model=PhysicalActivityResponse)
def get_physical_activity_route(activity_id: int, db: Session = Depends(get_db)):
    """Retrieves a physical activity record by its ID."""
    return get_activity_by_id(db, activity_id)

# Delete a physical activity record
@router.delete("/physical_activity/{activity_id}", response_model=dict)
def delete_physical_activity_route(activity_id: int, db: Session = Depends(get_db)):
    """Deletes a physical activity record by its ID."""
    return delete_activity(db, activity_id)
