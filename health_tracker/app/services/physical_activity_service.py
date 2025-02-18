import logging
from sqlalchemy.orm import Session
from app.db.models import PhysicalActivity
from pydantic import BaseModel
from datetime import date
from fastapi import HTTPException

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Pydantic model for validation
class PhysicalActivityCreate(BaseModel):
    user_id: int
    steps: int
    date: date

class PhysicalActivityResponse(BaseModel):
    id: int
    user_id: int
    steps: int
    date: date

    class Config:
        from_attributes = True

def create_activity(db: Session, activity: PhysicalActivityCreate):
    """
    Creates a new physical activity record.
    """
    logging.info(f"Creating activity for user {activity.user_id} on {activity.date}.")
    new_activity = PhysicalActivity(**activity.model_dump())
    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)
    logging.info("Activity record created successfully.")
    return new_activity

def get_all_activities(db: Session):
    """
    Retrieves all physical activity records.
    """
    logging.info("Fetching all physical activity records.")
    return db.query(PhysicalActivity).all()

def get_activity_by_id(db: Session, activity_id: int):
    """
    Retrieves a specific physical activity record by ID.
    """
    logging.info(f"Fetching activity record with ID {activity_id}.")
    activity = db.query(PhysicalActivity).filter(PhysicalActivity.id == activity_id).first()
    if not activity:
        logging.warning(f"Activity record with ID {activity_id} not found.")
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity

def delete_activity(db: Session, activity_id: int):
    """
    Deletes a specific physical activity record by ID.
    """
    logging.info(f"Deleting activity record with ID {activity_id}.")
    activity = db.query(PhysicalActivity).filter(PhysicalActivity.id == activity_id).first()
    if not activity:
        logging.warning(f"Activity record with ID {activity_id} not found.")
        raise HTTPException(status_code=404, detail="Activity not found")
    db.delete(activity)
    db.commit()
    logging.info("Activity record deleted successfully.")
    return {"message": "Activity deleted successfully"}
