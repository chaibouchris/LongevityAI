from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services.health_score_service import calculate_health_score
from app.services.system_health_average_service import update_system_average

router = APIRouter()

# Database session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Calculate user health score and update system average
@router.get("/get_health_score/{user_id}")
def get_health_score(user_id: int, db: Session = Depends(get_db)):
    """Calculates the health score for a given user and updates the system-wide average."""
    try:
        result = calculate_health_score(user_id, db)
        update_system_average(db)  # Update system average after calculation
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
