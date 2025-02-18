from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime, func
from app.db.database import Base

class HealthScore(Base):
    """
    Model representing a user's health score.
    """
    __tablename__ = "health_scores"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)  # Links to a user
    score = Column(Float, nullable=False)  # Health score value
    last_updated = Column(DateTime, default=func.now(), onupdate=func.now())  # Last updated timestamp