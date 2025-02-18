import logging
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from app.db.models import HealthScore, SystemHealthAverage

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def update_system_average(db: Session):
    """
    Calculates and stores a new system-wide health score average.
    """
    avg_score = db.query(func.avg(HealthScore.score)).scalar() or 0
    logging.info(f"Calculated new system health average: {avg_score}")

    # Inserts a new average entry instead of updating an existing record
    new_average_entry = SystemHealthAverage(average_score=avg_score)
    db.add(new_average_entry)
    db.commit()
    logging.info("New system health average recorded successfully.")

def get_latest_system_average(db: Session):
    """
    Retrieves the most recent system-wide health score average.
    """
    latest_avg = db.query(SystemHealthAverage).order_by(SystemHealthAverage.timestamp.desc()).first()
    if latest_avg:
        logging.info(f"Latest system health average retrieved: {latest_avg.average_score}")
        return latest_avg.average_score
    else:
        logging.warning("No system health average found, returning default value 0.")
        return 0
