import logging
from sqlalchemy.orm import Session
from app.db.models import SleepActivity
from pydantic import BaseModel
from datetime import date
from fastapi import HTTPException

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Pydantic model for validation
class SleepActivityCreate(BaseModel):
    user_id: int
    sleep_duration: float
    date: date

class SleepActivityResponse(BaseModel):
    id: int
    user_id: int
    sleep_duration: float
    date: date

    class Config:
        from_attributes = True

def create_sleep_record(db: Session, sleep: SleepActivityCreate):
    """
    Creates a new sleep activity record in the database.
    """
    logging.info(f"Creating sleep record for user {sleep.user_id} on {sleep.date}.")
    new_sleep = SleepActivity(**sleep.model_dump())
    db.add(new_sleep)
    db.commit()
    db.refresh(new_sleep)
    logging.info("Sleep record created successfully.")
    return new_sleep

def get_all_sleep_records(db: Session):
    """
    Retrieves all sleep activity records.
    """
    logging.info("Fetching all sleep activity records.")
    return db.query(SleepActivity).all()

def get_sleep_record_by_id(db: Session, sleep_id: int):
    """
    Retrieves a specific sleep activity record by its ID.
    """
    logging.info(f"Fetching sleep record with ID {sleep_id}.")
    sleep = db.query(SleepActivity).filter(SleepActivity.id == sleep_id).first()
    if not sleep:
        logging.warning(f"Sleep record with ID {sleep_id} not found.")
        raise HTTPException(status_code=404, detail="Sleep record not found")
    return sleep

def delete_sleep_record(db: Session, sleep_id: int):
    """
    Deletes a specific sleep activity record by its ID.
    """
    logging.info(f"Deleting sleep record with ID {sleep_id}.")
    sleep = db.query(SleepActivity).filter(SleepActivity.id == sleep_id).first()
    if not sleep:
        logging.warning(f"Sleep record with ID {sleep_id} not found.")
        raise HTTPException(status_code=404, detail="Sleep record not found")
    db.delete(sleep)
    db.commit()
    logging.info("Sleep record deleted successfully.")
    return {"message": "Sleep record deleted successfully"}
