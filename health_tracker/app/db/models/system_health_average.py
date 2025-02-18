from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.sql import func
from app.db.database import Base

class SystemHealthAverage(Base):
    """
    Model representing the system-wide average health score over time.
    """
    __tablename__ = "system_health_average"

    id = Column(Integer, primary_key=True, index=True)
    average_score = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=func.now(), onupdate=func.now())
