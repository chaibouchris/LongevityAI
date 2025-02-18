import logging
from sqlalchemy.orm import Session
from app.db.models import BloodTest
from pydantic import BaseModel
from datetime import date
from fastapi import HTTPException

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Pydantic model for validation
class BloodTestCreate(BaseModel):
    user_id: int
    glucose_level: float
    hemoglobin_level: float
    cholesterol_level: float
    creatinine_level: float
    white_blood_cell_count: float
    date: date

class BloodTestResponse(BaseModel):
    id: int
    user_id: int
    glucose_level: float
    hemoglobin_level: float
    cholesterol_level: float
    creatinine_level: float
    white_blood_cell_count: float
    date: date

    class Config:
        from_attributes = True

def create_blood_test(db: Session, test: BloodTestCreate):
    """
    Creates a new blood test record.
    """
    logging.info(f"Creating blood test record for user {test.user_id} on {test.date}.")
    new_test = BloodTest(**test.model_dump())
    db.add(new_test)
    db.commit()
    db.refresh(new_test)
    logging.info("Blood test record created successfully.")
    return new_test

def get_all_blood_tests(db: Session):
    """
    Retrieves all blood test records.
    """
    logging.info("Fetching all blood test records.")
    return db.query(BloodTest).all()

def get_blood_test_by_id(db: Session, test_id: int):
    """
    Retrieves a specific blood test record by ID.
    """
    logging.info(f"Fetching blood test record with ID {test_id}.")
    test = db.query(BloodTest).filter(BloodTest.id == test_id).first()
    if not test:
        logging.warning(f"Blood test record with ID {test_id} not found.")
        raise HTTPException(status_code=404, detail="Blood test not found")
    return test

def delete_blood_test(db: Session, test_id: int):
    """
    Deletes a specific blood test record by ID.
    """
    logging.info(f"Deleting blood test record with ID {test_id}.")
    test = db.query(BloodTest).filter(BloodTest.id == test_id).first()
    if not test:
        logging.warning(f"Blood test record with ID {test_id} not found.")
        raise HTTPException(status_code=404, detail="Blood test not found")
    db.delete(test)
    db.commit()
    logging.info("Blood test record deleted successfully.")
    return {"message": "Blood test deleted successfully"}
