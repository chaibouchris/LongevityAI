from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services.system_health_average_service import update_system_average, get_latest_system_average
from app.db.models import SystemHealthAverage

router = APIRouter()

# Database session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/calculate_system_health_average")
def calculate_and_update_system_average(db: Session = Depends(get_db)):
    """Calculates and updates the system-wide health score average."""
    try:
        update_system_average(db)
        return {"message": "System average updated successfully", "latest_average": get_latest_system_average(db)}
    except Exception as e:
        return {"error": str(e)}

@router.get("/get_latest_health_average")
def get_latest_average(db: Session = Depends(get_db)):
    """Retrieves the latest system-wide health score average."""
    latest_avg = get_latest_system_average(db)
    return {"latest_average": latest_avg}

@router.get("/get_health_average_history")
def get_health_average_history(
    db: Session = Depends(get_db),
    limit: int = Query(10, description="Number of records to retrieve", gt=0)
):
    """Retrieves historical health score averages, limited by a given number of records."""
    history = (
        db.query(SystemHealthAverage)
        .order_by(SystemHealthAverage.timestamp.desc())
        .limit(limit)
        .all()
    )
    return {"history": history}
